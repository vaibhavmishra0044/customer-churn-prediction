import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os

# Get the directory where app.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model and scaler
model = joblib.load(os.path.join(BASE_DIR, 'churn_model.pkl'))
scaler = joblib.load(os.path.join(BASE_DIR, 'scaler.pkl'))
# App title
st.title("Customer Churn Prediction App")
st.write("Enter customer details below to predict whether they will churn.")

# Input fields
st.header("Customer Details")

tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.slider("Monthly Charges ($)", 18, 119, 65)
total_charges = monthly_charges * tenure

senior_citizen = st.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.selectbox("Partner", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["No", "Yes"])
phone_service = st.selectbox("Phone Service", ["No", "Yes"])
paperless_billing = st.selectbox("Paperless Billing", ["No", "Yes"])
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])

# Predict button
if st.button("Predict Churn"):

    # Encode inputs
    senior = 1 if senior_citizen == "Yes" else 0
    part = 1 if partner == "Yes" else 0
    dep = 1 if dependents == "Yes" else 0
    phone = 1 if phone_service == "Yes" else 0
    paper = 1 if paperless_billing == "Yes" else 0
    gender = 0

    # Scale numerical
    numerical = scaler.transform([[tenure, monthly_charges, total_charges]])
    ten_scaled = numerical[0][0]
    mc_scaled = numerical[0][1]
    tc_scaled = numerical[0][2]

    # Build feature vector matching training columns
    features = {
        'gender': gender, 'SeniorCitizen': senior, 'Partner': part,
        'Dependents': dep, 'tenure': ten_scaled, 'PhoneService': phone,
        'PaperlessBilling': paper, 'MonthlyCharges': mc_scaled,
        'TotalCharges': tc_scaled,
        'MultipleLines_No phone service': 0, 'MultipleLines_Yes': 0,
        'InternetService_Fiber optic': 1 if internet_service == "Fiber optic" else 0,
        'InternetService_No': 1 if internet_service == "No" else 0,
        'OnlineSecurity_No internet service': 0, 'OnlineSecurity_Yes': 0,
        'OnlineBackup_No internet service': 0, 'OnlineBackup_Yes': 0,
        'DeviceProtection_No internet service': 0, 'DeviceProtection_Yes': 0,
        'TechSupport_No internet service': 0, 'TechSupport_Yes': 0,
        'StreamingTV_No internet service': 0, 'StreamingTV_Yes': 0,
        'StreamingMovies_No internet service': 0, 'StreamingMovies_Yes': 0,
        'Contract_One year': 1 if contract == "One year" else 0,
        'Contract_Two year': 1 if contract == "Two year" else 0,
        'PaymentMethod_Credit card (automatic)': 1 if payment_method == "Credit card (automatic)" else 0,
        'PaymentMethod_Electronic check': 1 if payment_method == "Electronic check" else 0,
        'PaymentMethod_Mailed check': 1 if payment_method == "Mailed check" else 0,
    }

    input_df = pd.DataFrame([features])
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.header("Prediction Result")
    if prediction == 1:
        st.error("⚠️ HIGH RISK! This customer is likely to churn!")
        st.write("Churn Probability:", round(probability * 100, 2), "%")
    else:
        st.success("✅ LOW RISK! This customer is likely to stay!")
        st.write("Churn Probability:", round(probability * 100, 2), "%")
