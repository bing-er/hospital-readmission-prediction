# 🏥 Predicting Hospital Readmission Risk Using Explainable Machine Learning on Public Health Data
## Overview
This project aims to predict 30-day hospital readmissions using the UCI Diabetes 130-Hospital dataset. We compare traditional ML models (Logistic Regression, Random Forest) and ensemble models (XGBoost) with explainability tools such as SHAP and LIME.

## 👥 Team Members and Roles

| **Member** | **Role** | **Responsibilities** |
|:--|:--|:--|
| **Binger** | Data Engineer / Preprocessing Lead | - Acquire and preprocess UCI Diabetes dataset.<br>- Handle missing values, encoding, and normalization.<br>- Perform exploratory data analysis (EDA) with descriptive statistics and visualizations. |
| **Savina** | Modeling & Evaluation Lead | - Implement baseline models (Logistic Regression, Random Forest).<br>- Tune and train advanced models (XGBoost, LightGBM).<br>- Evaluate models using AUC, F1, and calibration plots. |
| **Yansong** | Explainability & Reporting Lead | - Apply SHAP/LIME to interpret feature importance.<br>- Conduct fairness analysis across demographics.<br>- Prepare all visualizations, report sections, and final presentation slides. |


## 📝 Team Task Assignment for Proposal

| **Member** | **Main Writing Tasks** | **Supporting Tasks** |
|:--|:--|:--|
| **Binger** | Write Sections Keywords, 3 (Dataset Description) and 5 (Team Plan and Timeline); provide dataset summary, feature overview and figures | Create, compile and format the final proposal in Overleaf.|
| **Savina** | Write Section 4 (Exploratory Data Analysis); review EDA findings for statistical validity; contribute to discussion of model preparation and expected results. | Review Abstract & Expected Results for technical clarity. |
| **Yansong** | Write Sections 0–3 (Abstract, Introduction, Related Work). | Insert SHAP/LIME visuals (concept diagrams) and ensure citation formatting. |


## Project Timeline
| Phase | Dates | Deliverables |
|:--|:--|:--|
| Proposal | Nov 1 – Nov 13 | 3-page IEEE-style proposal |
| Modeling | Nov 14 – Nov 27 | Baseline & advanced models |
| Final Report | Nov 28 – Dec 4 | Full report + presentation |


## Folder Structure
```text
hospital-readmission-prediction/
│
├── data/
│   ├── raw/                    # Binger - original datasets
│   └── processed/              # Binger - cleaned data
│
├── notebooks/
│   ├── 01_eda.ipynb             # Binger – data cleaning, EDA
│   ├── 02_modeling.ipynb        # Savina – baseline & advanced models
│   └── 03_explainability.ipynb  # Yansong – SHAP/LIME
│
├── src/
│   ├── data_preprocessing.py  # Binger
│   ├── model_training.py      # Savina
│   ├── model_evaluation.py    # Savina
│   └── explainability.py      # Yansong
│
├── results/
│   ├── figures/            # Shared (ROC, PR, SHAP plots etc.)
│   ├── metrics/            # Savina - model results
│   └── reports/            # Yansong - draft PDFs
│
├── docs/
│   ├── proposal/           # Yansong - IEEE 3-apge proposal (Nov 13)
│   ├── final_report/       # All - final report (Dec 4)
│   └── presentation/       # All - slides for presentation
│
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
