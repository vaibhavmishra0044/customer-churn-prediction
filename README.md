# 🔮 Customer Churn Prediction

An end-to-end machine learning project that predicts whether a telecom customer will churn using Python, Scikit-learn, and XGBoost. Built with real-world data and deployed as an interactive web application.

---

## 📌 Problem Statement

Customer churn is one of the biggest challenges in the telecom industry. Acquiring a new customer costs 5-7x more than retaining an existing one. This project builds a machine learning model that identifies at-risk customers before they leave, enabling businesses to take proactive retention actions.

---

## 📊 Dataset

- **Source:** Telco Customer Churn Dataset (Kaggle)
- **Size:** 7,043 customers | 21 features
- **Target Variable:** Churn (Yes/No)

---

## 🔍 Key Findings

| Insight | Finding |
|---|---|
| Month-to-month contracts | 42.7% churn rate vs 2.8% for two-year contracts |
| New customers (0-12 months) | Highest churn rate of 47.7% |
| Fiber optic customers | Churn more despite premium service |
| Electronic check users | Highest churn rate among payment methods |
| Senior citizens | Churn at 41.7% vs 23.6% for non-seniors |

---

## 🤖 Model Results

| Model | Accuracy | ROC-AUC |
|---|---|---|
| Logistic Regression | 79.32% | 88.18% |
| Random Forest | **84.49%** | **91.94%** |
| XGBoost | 82.71% | 90.59% |

**Best Model: Random Forest with 91.94% ROC-AUC Score**

---

## 💼 Business Recommendations

1. **Target month-to-month customers** — Offer discounts to switch to annual plans
2. **Focus on new customers (0-12 months)** — Implement strong onboarding program
3. **Address fiber optic dissatisfaction** — Investigate service quality and pricing
4. **Convert electronic check users** — Incentivize automatic payment methods
5. **Senior citizen retention program** — Create dedicated support and special pricing

---

## 🛠️ Tech Stack

- **Languages:** Python
- **ML Libraries:** Scikit-learn, XGBoost, SHAP
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Web App:** Streamlit
- **Version Control:** Git, GitHub

---

## 📁 Project Structure