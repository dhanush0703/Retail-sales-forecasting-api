# Retail Sales Forecasting API

> **An end-to-end demand forecasting pipeline** (feature engineering → model training & hyperparameter tuning → evaluation & explainability → REST API deployment) built with Python, XGBoost (Optuna tuning) and FastAPI.  
> Designed to help retail/FMCG teams (inventory planners, demand planners, supply chain) make more accurate store-level sales forecasts and reduce stockouts/overstock, lowering costs and waste.

---

## 🌍 Project Overview  
Retail and FMCG companies (like **Henkel**) rely heavily on **accurate demand forecasting** to manage supply chains, optimize production, reduce waste, and ensure product availability.  

This project builds an **end-to-end pipeline** for forecasting retail sales:  
1. **Data Preprocessing** – cleaning, feature engineering, handling missing values  
2. **Model Training** – machine learning models for demand forecasting  
3. **Hyperparameter Tuning** – to achieve the best RMSE  
4. **Evaluation** – detailed analysis of model performance  
5. **Deployment** – exposing the trained model as a REST API using **FastAPI**  

---

## 🎯 Business Problem  
- Overstocking ➝ leads to higher storage costs & wastage.  
- Understocking ➝ results in lost sales & unhappy customers.  
- Seasonal demand, promotions, and holidays make forecasting more complex.  

An **intelligent forecasting system** provides:  
✔️ Better inventory planning  
✔️ Reduced operational costs  
✔️ Sustainability through waste reduction  
✔️ Improved customer satisfaction  

---

## 🛠️ Workflow  

### **1️⃣ Data Preprocessing**  
- Imported sales data and created features like:  
  - Date-based features (day, month, year, week, weekday, season)  
  - Holiday and promotion indicators  
- Generated lag and moving average features (`Sales_Lag1`, `Sales_MA3`, `Sales_MA7`, etc.)  
- Standardized numeric features (Fuel_Price, CPI, Temperature).  
- One-hot encoded categorical features (`Type`, `Season`).  

### **2️⃣ Model Training & Hyperparameter Tuning**  
- Models tried: **Linear Regression, Random Forest, XGBoost**  
- Used **Optuna** to tune XGBoost hyperparameters (`n_estimators`, `learning_rate`, `max_depth`, etc.).  
- Objective: minimize validation **RMSE**.  

### **3️⃣ Model Evaluation**  
- **Metrics:** RMSE, MAE, R²  
- **Baseline RMSE:** ~3500  
- **After tuning (Optuna):** RMSE improved to **3138.7**  
- **Improvement:** ~10% lower error, meaning forecasts are ~360 units closer to actual sales.  

### **4️⃣ Deployment with FastAPI**  
- Exposed trained model as a **REST API**.  
- Endpoint: `POST /predict` → returns forecasted sales for given input features.  
- Interactive Swagger docs available at `/docs`.  

---
## 📊 Results  
- **Best Model:** XGBoost Regressor (tuned with Optuna)  
- **RMSE:** 3138.7 (from 3500 baseline)  
- **Business Interpretation:** For a store selling ~30,000 units weekly, this means forecast error dropped from ~11.6% to ~10.4%. Across multiple stores, this saves thousands of units from being misallocated, reducing waste and improving customer satisfaction.  

---
## ⚙️ Installation & Usage  

Clone the repository:
```bash
git clone https://github.com/dhanush0703/Retail-sales-forecasting-api.git
cd Retail-sales-forecasting-api
```

Create a virtual environment & install dependencies:
```bash
pip install -r requirements.txt
```

Run the API locally:
```bash
uvicorn main:app --reload
```

Access the interactive API docs at:  
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  

---
---

## 🌟 Future Improvements  
- 🔮 Add LSTM / Prophet models for seasonality  
- 🐳 Dockerize for cloud deployment  
- ☁️ Deploy on AWS/GCP/Azure  
- 📦 Extend to multi-store, multi-product forecasts  
- ♻️ Align with Company’s sustainability goals by reducing waste via accurate forecasts  
---

✨ With this project, I demonstrate how **Machine Learning, Hyperparameter Tuning, and API deployment** can solve real-world retail forecasting problems — making supply chains **smarter, sustainable, and efficient**.  
