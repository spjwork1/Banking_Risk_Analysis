# 🏦 Banking Data Analysis & Customer Risk Prediction

This repository delivers an end-to-end solution for banking customer risk analytics, combining **Exploratory Data Analysis (EDA)**, **Business Intelligence (BI) Dashboarding (Power BI)**, and **Production-Ready Predictive Modeling**. The goal is to transform raw banking data into actionable business intelligence, supporting risk-aware lending, customer segmentation, and operational insights for financial institutions.[1][2]

***

## 📁 Project Structure

- `BankEDA(version 2).ipynb` – Jupyter Notebook for thorough EDA and feature engineering
- `train_model.py` – Script to train and evaluate the predictive model (Random Forest)
- `requirements.txt` – Required dependencies
- `/powerbi_dashboard/` – Power BI `.pbix` files for interactive, business-ready dashboards
- `/data/` – Clean banking datasets
- `README.md` – Project documentation

***

## 🧠 Solution Overview

### 1️⃣ Data Analysis (EDA)

Conducted in Jupyter Notebook, leveraging **Python (Pandas, NumPy)**:

- Cleansing/validation for real-world banking data
- Exploratory statistics, feature correlations, outlier handling
- Deep segmentation: demographics, financial standing, credit risk, etc.
- Advanced visualization (Seaborn, Matplotlib) for stakeholder communication

### 2️⃣ BI Dashboards (Power BI)

- Dashboarding KPIs: risk scores, churn rates, profitability analysis
- Interactive filtering (customer cohorts, loan products, geographic splits)
- Financial performance and compliance views
- Built for decision makers: product managers, analysts, risk teams

### 3️⃣ Predictive Risk Modeling

Delivered in `train_model.py` using **scikit-learn**:

- Model: Random Forest Classifier (extendable to other ML approaches)
- Target: Predict risk category/default likelihood for new or existing customers
- Output: Classification reports, confusion matrix, serialized model via joblib for API and integration
- Ready for deployment to web/API

***

## ⚙️ Quickstart Guide

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/banking-analysis.git
   cd banking-analysis
   ```
2. **Set up environment:**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```
3. **Install dependencies:**
   
4. **Run EDA notebook:**
   ```bash
   jupyter lab
   ```
   Open `BankEDA(version 2).ipynb`, follow analysis steps.
5. **Train predictive model:**
   ```bash
   python train_model.py
   ```
   Model output and evaluation metrics will be displayed.

***

## 📊 Power BI Dashboard

The interactive dashboard (in `/powerbi_dashboard/`) enables business analysts and leadership to review risk, performance, and customer segmentation.  
**Instructions:**
- Open **Power BI Desktop**
- Load `.pbix` file from project directory
- Use interactive controls (filters, drilldowns) for tailored insights

***

## 🚀 Deployment & Roadmap

- **Web integration:** Plan to expose predictions and visual analytics via a unified web portal (Flask/FastAPI/Streamlit)
- **API endpoints:** Deploy ML model for real-time risk prediction (REST API)
- **Embedded analytics:** Integrate with enterprise BI platforms or client portals
- **Automation:** Pipeline for periodic data refresh and retraining

***

## 🧰 Technology Stack

| Layer                 | Tools                           |
| --------------------- | ------------------------------ |
| Data Analysis         | Python, Pandas, NumPy           |
| BI Visualization      | Power BI, Matplotlib, Seaborn   |
| ML Modeling           | scikit-learn (Random Forest)    |
| Model Persistence     | joblib                          |
| API / Web Interface   | (Planned) Flask, Streamlit      |
| Workspace             | JupyterLab                      |

***

## 👨‍💻 Author

**Sumanyu**  
Contact: [spjwork1@gmail.com](mailto:spjwork1@gmail.com)  

***

## 📝 License

MIT License.

***
