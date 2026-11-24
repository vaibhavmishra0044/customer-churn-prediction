# Customer Churn Prediction | Telecom Analytics

**Business analytics • Customer retention • Predictive modeling**

An end-to-end analytics and machine learning project exploring why telecom customers leave and how businesses can identify customers at risk of churn.

## Project at a glance

| Dataset | Target | Best reported model | Reported ROC-AUC |
| --- | --- | --- | --- |
| 7,043 customers, 21 columns | Churn (Yes/No) | Random Forest | 91.94% |

## Business objective

Identify customer segments with elevated churn, compare classification models, and translate analytical findings into actionable retention strategies.

## Dataset and analytical approach

- Source: Telco Customer Churn dataset (Kaggle).
- Explore customer demographics, tenure, contract types, services, charges and payment methods.
- Compare churn rates across customer segments.
- Compare Logistic Regression, Random Forest and XGBoost using accuracy and ROC-AUC.
- Translate findings into retention recommendations and support interactive prediction with Streamlit.

## Key findings and business recommendations

| Reported finding | Recommended action |
| --- | --- |
| Month-to-month contracts: 42.7% churn vs 2.8% for two-year contracts | Test incentives for longer contracts. |
| Customers with 0–12 months of tenure: 47.7% churn | Strengthen onboarding and early customer engagement. |
| Higher churn among fiber optic customers | Investigate pricing, service quality and customer feedback. |
| Electronic check users show elevated churn | Test convenient alternative payment options. |
| Senior citizens: 41.7% churn vs 23.6% for other customers | Investigate accessibility and support needs. |

These are observed associations, not proof of causation. Proposed interventions should be tested before rollout.

## Model comparison

| Model | Reported accuracy | Reported ROC-AUC |
| --- | ---: | ---: |
| Logistic Regression | 79.32% | 88.18% |
| Random Forest | **84.49%** | **91.94%** |
| XGBoost | 82.71% | 90.59% |

Figures are retained from the original project documentation; they have not been independently reproduced in this README update. Before operational use, validate the split methodology, leakage controls, precision, recall and probability calibration.

## Technology stack

Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, XGBoost, SHAP and Streamlit.

## Getting started

```bash
git clone https://github.com/vaibhavmishra0044/customer-churn-prediction.git
cd customer-churn-prediction
python -m pip install -r requirements.txt
```

Explore the [repository files](https://github.com/vaibhavmishra0044/customer-churn-prediction/tree/main) for the analysis and application assets.

## Next steps

- Validate performance on an untouched test set.
- Evaluate retention campaign costs and expected benefits.
- Monitor model performance and customer behavior over time.

## Author

[Vaibhav Mishra](https://github.com/vaibhavmishra0044) | [LinkedIn](https://linkedin.com/in/vaibhav-mishra04)
