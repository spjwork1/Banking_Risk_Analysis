import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import joblib

# Load data
df = pd.read_csv("Banking.csv")

# Define features to use (must match your csv column names)
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

# Drop rows with missing values in features
df = df.dropna(subset=features)

# Extract features for clustering
X = df[features]

# Scale features for meaningful cluster distances
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Choose number of clusters (adjust as needed)
num_clusters = 3

# Fit KMeans clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
cluster_labels = kmeans.fit_predict(X_scaled)

# Save scaler and model
joblib.dump(scaler, "scaler.pkl")
joblib.dump(kmeans, "kmeans_model.pkl")

print(f"Model trained with {num_clusters} clusters and saved as 'kmeans_model.pkl'.")
print("Scaler saved as 'scaler.pkl'.")
print("Cluster size distribution:")
print(pd.Series(cluster_labels).value_counts())
