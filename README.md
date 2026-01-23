# Retail Demand Forecasting Workshop

**Role:** Contributor | AI/ML Engineer Intern Level Project

This project focuses on **forecasting daily retail product demand** using historical sales data. The goal is to provide actionable insights for inventory management and sales planning through predictive modeling.

---

## 📂 Project Overview

Retail businesses face challenges in managing stock and anticipating demand. This project demonstrates **end-to-end forecasting workflow** using Python and machine learning techniques.

Key objectives:
- Understand historical sales patterns
- Forecast daily demand at item/outlet level
- Evaluate model performance and business impact

---

## 🗃 Dataset

- **Source:** Workshop-provided dataset  
- **Description:** Contains historical sales data for multiple products and outlets, including:
  - Date  
  - Item ID / Product  
  - Outlet ID  
  - Sales Quantity / Revenue  

- **Preprocessing Steps:**
  - Missing value handling  
  - Feature engineering (e.g., day of week, lag features)  
  - Aggregations for modeling

---

## 🛠 Workflow & Approach

1. **Exploratory Data Analysis (EDA)**  
   - Identify trends, seasonality, and outliers  
   - Visualize demand patterns across outlets and products

2. **Feature Engineering**  
   - Time-based features (day, week, month)  
   - Lag features to capture demand patterns  
   - Categorical encoding for item/outlet IDs

3. **Model Building**  
   - Regression-based models (XGBoost, Random Forest)  
   - Train-test split for validation  
   - Hyperparameter tuning to improve accuracy

4. **Evaluation**  
   - Metrics used: **MAPE, RMSE**  
   - Comparison with baseline methods  
   - Visualizations of predicted vs actual demand

---

## 📈 Results

- Successfully predicted daily demand with minimal error  
- Identified under-forecast and over-forecast scenarios  
- Provided insights for **buffer stock adjustments** and **inventory optimization**  

> Example: Using the model predictions, the workshop highlighted opportunities to reduce stock-outs by 15% while avoiding overstock.

---

## 💡 Key Learnings

- Understanding the business problem is critical before modeling  
- Data preprocessing and feature engineering significantly impact accuracy  
- Model evaluation must align with business goals (MAPE over RMSE for inventory)  
- Clear documentation of results helps stakeholders make informed decisions

---

## 🔧 Tools & Libraries

- **Programming:** Python  
- **Data Analysis:** Pandas, NumPy  
- **Visualization:** Matplotlib, Seaborn  
- **Machine Learning:** XGBoost, Scikit-learn  
- **Development:** Jupyter Notebook, Git/GitHub

---

## 👨‍💻 My Contribution

- Implemented **data cleaning and preprocessing** steps  
- Conducted **EDA and feature engineering** for improved model performance  
- Built and evaluated regression-based forecasting models  
- Documented findings and provided clear visualizations for presentation

---

## 📌 How to Run

1. Clone the repo:  
   ```bash
   git clone https://github.com/Kalingu/retail-demand-forecasting-workshop_kalingu.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Open and run notebooks in Jupyter:  
   ```bash
   jupyter notebook notebooks/analysis.ipynb
   ```
