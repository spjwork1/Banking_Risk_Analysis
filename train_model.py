import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load CSV data
df = pd.read_csv("Banking.csv")

# Define features and target - make sure exact column names are used
features = [
    "Estimated Income",
    "Superannuation Savings",
    "Amount of Credit Cards",
    "Credit Card Balance",
    "Bank Loans",
    "Bank Deposits",
    "Checking Accounts",
    "Saving Accounts",
    "Foreign Currency Account",
    "Business Lending"
]

df = df.dropna(subset=features + ["Risk Weighting"])

X = df[features]
y = df["Risk Weighting"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train XGBoost regressor
model = xgb.XGBRegressor(
    n_estimators=300,
    max_depth=6,
    learning_rate=0.1,
    random_state=42
)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R^2 Score:", r2_score(y_test, y_pred))

# Save the model for later use in Streamlit app
joblib.dump(model, "risk_xgb_model.pkl")
print("Model saved as risk_xgb_model.pkl")
