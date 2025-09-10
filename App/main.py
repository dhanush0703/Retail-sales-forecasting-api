from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from typing import Optional

# Load your saved pipeline (must be fitted pipeline)
pipeline = joblib.load("models/sales_model_pipeline2.pkl")  # relative path

# Initialize FastAPI
app = FastAPI(title="Sales Prediction API")

# --------------------------
# Input schema
# --------------------------
class StoreWeekInput(BaseModel):
    Sales_Lag1: float
    Sales_Lag2: float
    Sales_MA3: float
    Sales_MA7: float
    Fuel_Price: float
    Temperature: float
    CPI: float
    Week: int
    Month: int
    Day: int
    IsHoliday_x: int

# --------------------------
# Prediction endpoint
# --------------------------
@app.post("/predict")
def predict_sales(data: StoreWeekInput):
    input_df = pd.DataFrame([data.dict()])
    pred = pipeline.predict(input_df)
    return {"Predicted_Sales": float(pred[0])}

# --------------------------
# What-if schema
# --------------------------
class WhatIfInput(StoreWeekInput):
    fuel_increase_pct: float = 0.0
    markdown_increase_pct: float = 0.0
    toggle_holiday: Optional[int] = None

# --------------------------
# What-if endpoint
# --------------------------
@app.post("/whatif")
def whatif_sales(data: WhatIfInput):
    input_df = pd.DataFrame([data.dict()])

    # Base prediction
    base_pred = float(pipeline.predict(input_df)[0])

    # Scenario copy
    scenario_df = input_df.copy()

    # Apply % adjustments
    if data.fuel_increase_pct != 0:
        scenario_df["Fuel_Price"] *= (1 + data.fuel_increase_pct / 100.0)

    if data.markdown_increase_pct != 0:
        scenario_df["Sales_MA3"] *= (1 + data.markdown_increase_pct / 100.0)
        scenario_df["Sales_MA7"] *= (1 + (data.markdown_increase_pct * 0.8) / 100.0)

    # Holiday toggle
    if data.toggle_holiday is not None:
        scenario_df["IsHoliday_x"] = data.toggle_holiday

    # Scenario prediction
    scenario_pred = float(pipeline.predict(scenario_df)[0])

    # Delta & impact
    delta = scenario_pred - base_pred
    impact = (delta / base_pred) * 100 if base_pred != 0 else 0

    return {
        "Base_Predicted_Sales": base_pred,
        "Scenario_Predicted_Sales": scenario_pred,
        "Delta": delta,
        "Impact": f"{impact:+.2f}%",
        "Fuel_Price_Adjusted": float(scenario_df["Fuel_Price"].iloc[0]),
        "Sales_MA3_Adjusted": float(scenario_df["Sales_MA3"].iloc[0]),
        "Sales_MA7_Adjusted": float(scenario_df["Sales_MA7"].iloc[0]),
        "IsHoliday_Adjusted": int(scenario_df["IsHoliday_x"].iloc[0]),
    }
