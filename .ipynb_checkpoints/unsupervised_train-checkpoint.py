import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("Banking.csv")
df = df[["Bank Loans(All combined)", "Credit Card Balance(monthly)", "Estimated Income(Annual)", "Superannuation Savings", "Amount of Credit Cards(integer count)"]]
df = df.dropna()

# Feature scaling is highly recommended (StandardScaler)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# Cluster into 3 groups (for example: low, medium, high risk)
kmeans = KMeans(n_clusters=3, random_state=42)
df["RiskCluster"] = kmeans.fit_predict(X_scaled)

# Now, analyze each cluster
print(df.groupby("RiskCluster").mean())
