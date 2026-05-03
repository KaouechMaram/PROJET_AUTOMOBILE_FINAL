# Automotive Industry Analysis & Forecasts (2030)

---

## 📌 Overview
End-to-end data science project analyzing the global automotive industry from 2010 to 2023, with forecasts up to 2030.  
The project focuses on the transition to electric vehicles (EV) and the impact of U.S. policies.

---

## 🚀 Key Results
- Developed **9 interactive dashboards** (from executive to technical views)  
- Built **6 machine learning models**:
  - XGBoost
  - Prophet
  - ARIMA
  - Linear Regression
  - Ensemble model (**best performance**)

- Best model: **Ensemble (R² = 0.91)**  

- Designed **9 future scenarios** based on:
  - Policy changes  
  - EV adoption rates  
  - Supply chain risks  

---

## 📊 Key Insights
- Best-case scenario: **Rapid EV transition (+10.4%)**  
- Main driver: **Raw material prices (28% importance)**  
- Optimal strategy: **Gradual EV transition**  
- Major risk: **Supply chain concentration**  

---

## 🛠️ Tech Stack
- **Language:** Python  
- **Libraries:** pandas, numpy, scikit-learn, xgboost, prophet, statsmodels  
- **Visualization:** Plotly (interactive dashboards)  
- **ML Techniques:** Regression, time series forecasting, ensemble modeling  

---

## 📁 Project Structure
code/ # Analysis and ML pipelines
dashboards/ # Interactive HTML dashboards
data/ # Dataset (12K+ rows)
models/ # Trained models (.pkl)
reports/ # PDF and Excel reports


---

## ▶️ How to Run
```bash
cd code
pip install -r requirements.txt
python run_analysis.py
