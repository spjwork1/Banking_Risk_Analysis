{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "211d070a-7e1d-4a19-a503-dd4935a5cdc0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MSE: 0.61\n",
      "R2: 0.54\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "['risk_model_5factors.pkl']"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.metrics import mean_squared_error, r2_score\n",
    "import joblib\n",
    "\n",
    "# Load data\n",
    "df = pd.read_csv('Banking.csv')\n",
    "\n",
    "# Select important features and target\n",
    "feature_cols = [\n",
    "    'Bank Loans',\n",
    "    'Credit Card Balance',\n",
    "    'Estimated Income',\n",
    "    'Superannuation Savings',\n",
    "    'Amount of Credit Cards'\n",
    "]\n",
    "target_col = 'Risk Weighting'\n",
    "\n",
    "# Basic cleaning (handle missing values)\n",
    "X = df[feature_cols].fillna(df[feature_cols].median())\n",
    "y = df[target_col].fillna(df[target_col].median())\n",
    "\n",
    "# Split data\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "# Model\n",
    "model = RandomForestRegressor(n_estimators=100, random_state=42)\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "# Evaluate\n",
    "y_pred = model.predict(X_test)\n",
    "print(f\"MSE: {mean_squared_error(y_test, y_pred):.2f}\")\n",
    "print(f\"R2: {r2_score(y_test, y_pred):.2f}\")\n",
    "\n",
    "# Save model\n",
    "joblib.dump(model, \"risk_model_5factors.pkl\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4549af17-07c9-4d00-aa93-0537ecda55ab",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
