import streamlit as st
import joblib
import numpy as np

st.title("Risk Weighting Predictor (0=Lowest Risk, 10=No Repayment)")

fields = [
    "Bank Loans(All combined)",
    "Credit Card Balance(monthly)",
    "Estimated Income(Annual)",
    "Superannuation Savings",
    "Amount of Credit Cards(integer count)"
]

inputs = []
for field in fields:
    val = st.text_input(f"{field}:")
    inputs.append(val)

def risk_message(score):
    if score < 3:
        return "Low Risk: Customer is very likely to repay."
    elif score < 6:
        return "Moderate Risk: Monitor customer account for any changes."
    elif score < 8:
        return "High Risk: Customer is likely to delay or miss repayment."
    else:
        return "Critical Risk: Customer is very unlikely to repay, strong caution advised."

if st.button("Predict Risk Weighting"):
    try:
        arr = np.array([float(x.strip()) for x in inputs]).reshape(1, -1)
        model = joblib.load("risk_model_5factors.pkl")
        pred = model.predict(arr)[0]
        st.success(f"Predicted Risk Weighting: {pred:.2f} (0 = lowest risk, 10 = no repayment)")
        st.info(risk_message(pred))
    except ValueError:
        st.error("Please enter valid numeric values for all fields.")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
