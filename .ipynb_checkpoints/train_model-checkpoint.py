import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import joblib

# Step 1: Load the dataset
df = pd.read_csv("Banking.csv")

# Step 2: Select key features for risk profiling
features = [
    "Bank Loans(All combined)",
    "Credit Card Balance(monthly)",
    "Estimated Income(Annual)",
    "Superannuation Savings",
    "Amount of Credit Cards(integer count)"
]

# Step 3: Basic cleaning - drop rows with missing values in the important columns
df = df[features].dropna()

# Step 4: Feature scaling - very important for clustering algorithms
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# Step 5: Train KMeans clustering model to segment customers into 3 risk groups
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)

# Optional: Analyze cluster centers for business understanding
print("Cluster centers (scaled features):")
print(kmeans.cluster_centers_)

# Step 6: Save model and scaler for later use
joblib.dump(kmeans, "risk_kmeans.pkl")
joblib.dump(scaler, "risk_scaler.pkl")

print("Model and scaler saved. Training complete.")
