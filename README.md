# 🏦 Banking Data Analysis & Customer Risk Prediction

This project performs **Exploratory Data Analysis (EDA)**, **Business Intelligence Dashboarding (Power BI)**, and **Predictive Modeling** on banking customer data to extract actionable insights for business decision-making.

It combines:

* Data understanding and cleaning using **Pandas, NumPy**
* Interactive visualizations with **Power BI**
* Machine learning model for predicting **risky customers** using **Random Forest**
* A future web-based interface for integrated analysis and dashboard viewing

---

## 📁 Project Structure

BankEDA(version 2).ipynb      → Main Jupyter Notebook for data analysis
train_model.py                → Predictive model (Random Forest) training script
requirements.txt              → Dependencies for the project
/powerbi_dashboard/           → Power BI .pbix files (interactive BI dashboard)
/data/                        → Banking dataset(s)
README.md                     → Project documentation

---

## 🧠 Project Overview

### 1️⃣ Exploratory Data Analysis

Performed in **BankEDA(version 2).ipynb**

* Data cleaning and preprocessing
* Feature correlation and distribution analysis
* Customer segmentation insights (age, balance, credit score, etc.)
* Visualization using Seaborn and Matplotlib

### 2️⃣ Business Intelligence Dashboard

Developed in **Power BI**

* Key performance indicators (KPIs)
* Customer demographics and churn visualizations
* Financial performance dashboards
* Drill-down and filter features for business exploration

### 3️⃣ Predictive Modeling

Implemented in **train_model.py**

* Model: Random Forest Classifier
* Objective: Predict risky or default-prone customers
* Evaluation metrics: Accuracy, Confusion Matrix, Classification Report
* Model saved via joblib for later web or API integration

---

## ⚙️ Setup Instructions

### Step 1: Clone the repository

git clone [https://github.com/](https://github.com/)<your-username>/banking-analysis.git
cd banking-analysis

### Step 2: Create and activate a virtual environment (recommended)

python -m venv venv
venv\Scripts\activate    # For Windows
source venv/bin/activate # For macOS/Linux

### Step 3: Install dependencies

pip install -r requirements.txt

### Step 4: Run the notebook for EDA

jupyter lab
Then open **BankEDA(version 2).ipynb**.

### Step 5: Train the predictive model

python train_model.py
This will train a Random Forest model and display accuracy and confusion matrix.

---

## 📊 Power BI Dashboard

The Power BI dashboard file (`.pbix`) can be found inside `/powerbi_dashboard/`.

To view:

1. Open **Power BI Desktop**
2. Click **File → Open**
3. Select the `.pbix` file
4. Interact with the visual dashboard

---

## 🚀 Future Plans

* Integrate the Power BI report and ML predictions into a unified **web interface**
* Deploy predictive model as a REST API (Flask/FastAPI)
* Host the dashboard using **Streamlit or Power BI Embedded**
* Automate data updates for real-time insights

---

## 🧰 Tech Stack

| Layer                   | Tools                         |
| ----------------------- | ----------------------------- |
| **Data Analysis**       | Python, Pandas, NumPy         |
| **Visualization**       | Matplotlib, Seaborn, Power BI |
| **Machine Learning**    | Scikit-learn (Random Forest)  |
| **Model Persistence**   | Joblib                        |
| **Interface (Planned)** | Streamlit / Flask             |
| **Environment**         | JupyterLab                    |

---

## ✨ Author

**Sumanyu**
📧 spjwork1@gmail.com
💼 Data & BI Enthusiast | Building Intelligent Systems for Business Decisions

---

## 📝 License

This project is open source and available under the **MIT License**.

