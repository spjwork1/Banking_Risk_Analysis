{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "211d070a-7e1d-4a19-a503-dd4935a5cdc0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MSE: 0.5193570000000001\n",
      "R2: 0.607023235773212\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "['risk_model.pkl']"
      ]
     },
     "execution_count": 3,
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
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state\n"
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
