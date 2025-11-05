import streamlit as st
import joblib
import numpy as np

st.set_page_config(layout="wide")
st.sidebar.title("Navigation")
option = st.sidebar.radio(
    "Select View:",
    ("Exploratory Data Analysis", "Clustering Prediction", "ML Model Explanation")
)

if option == "Exploratory Data Analysis":
    st.header("Exploratory Data Analysis")
    try:
        with open("BankEDA (Version 2).html", "r", encoding="utf-8") as f:
            html = f.read()
            html = html.replace('<body>', '<body style="width:100%;">')
            st.components.v1.html(html, scrolling=True, height=1000)
    except Exception as e:
        st.error(f"Could not load EDA notebook HTML: {e}")

elif option == "Clustering Prediction":
    st.title("Customer Segmentation")

    fields = [
        {"label": "Estimated Income (INR)", "help": "Annual estimated income."},
        {"label": "Superannuation Savings (INR)", "help": "Total retirement savings."},
        {"label": "Amount of Credit Cards", "help": "Number of credit cards held."},
        {"label": "Credit Card Balance (INR)", "help": "The balance you owe on your credit card, not the credit limit."},
        {"label": "Bank Loans (INR)", "help": "Total outstanding bank loans."},
        {"label": "Bank Deposits (INR)", "help": "Bank deposits held."},
        {"label": "Checking Accounts (INR)", "help": "Balance in checking accounts."},
        {"label": "Saving Accounts (INR)", "help": "Balance in saving accounts."},
        {"label": "Foreign Currency Account (INR)", "help": "Balance in foreign currency accounts."},
        {"label": "Business Lending (INR)", "help": "Outstanding business lending."}
    ]

    user_inputs = []
    for field in fields:
        val = st.text_input(field["label"], help=field["help"])
        user_inputs.append(val)

    if st.button("Assign Cluster"):
        try:
            input_data = np.array([float(x.replace(",", "").strip()) for x in user_inputs]).reshape(1, -1)
            scaler = joblib.load("scaler.pkl")
            kmeans = joblib.load("kmeans_model.pkl")

            input_scaled = scaler.transform(input_data)
            cluster_id = kmeans.predict(input_scaled)[0]

            st.success(f"Assigned Cluster ID: {cluster_id}")

            cluster_info = {
                0: "Cluster 0: Low risk, stable financial profile.",
                1: "Cluster 1: Moderate risk, average financial profile.",
                2: "Cluster 2: High risk, high liabilities."
            }
            st.info(cluster_info.get(cluster_id, "Unknown cluster"))

        except ValueError:
            st.error("Please enter valid numeric values for all fields.")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

elif option == "ML Model Explanation":
    st.header("ML Model Explanation: KMeans Clustering")
    st.markdown("""
### Model Method:
KMeans clustering is an unsupervised learning algorithm that partitions the data into distinct groups (clusters) based on feature similarity.

### Model Input Features:
- Estimated Income (INR)
- Superannuation Savings (INR)
- Amount of Credit Cards
- Credit Card Balance (INR)
- Bank Loans (INR)
- Bank Deposits (INR)
- Checking Accounts (INR)
- Saving Accounts (INR)
- Foreign Currency Account (INR)
- Business Lending (INR)

### Parameters:
- Number of Clusters (k): 3
- Initialization: k-means++ for better cluster center initialization
- Scaling: StandardScaler applied to normalize feature scales

### Purpose:
- To segment customers into risk/financial profiles without pre-labeled "risk" targets.
- Helps marketing, risk management, and customer support teams tailor strategies to different groups.

### How it Works:
- The algorithm assigns each customer data point to the nearest cluster centroid.
- Centroids are iteratively updated to minimize within-cluster variance.
- The output is a cluster ID indicating group membership.

### Benefits:
- Does not require labeled data.
- Detects natural groupings in financial data.
- Simplifies complex customer profiles into actionable segments.

### Notes:
- You can adjust the number of clusters by retraining with a different “k”.
- Interpret cluster characteristics based on centroid financial values.
    """)

