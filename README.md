# 🏥 Predicting Hospital Readmissions Using Public Health Data

## Overview
This project aims to predict 30-day hospital readmissions using the UCI Diabetes 130-Hospital dataset. We compare traditional ML models (Logistic Regression, Random Forest) and ensemble models (XGBoost) with explainability tools such as SHAP and LIME.

## 👥 Team Members and Roles

| **Member** | **Role** | **Responsibilities** |
|:--|:--|:--|
| **Binger** | Data Engineer / Preprocessing Lead | - Acquire and preprocess UCI Diabetes dataset.<br>- Handle missing values, encoding, and normalization.<br>- Perform exploratory data analysis (EDA) with descriptive statistics and visualizations. |
| **Savina** | Modeling & Evaluation Lead | - Implement baseline models (Logistic Regression, Random Forest).<br>- Tune and train advanced models (XGBoost, LightGBM).<br>- Evaluate models using AUC, F1, and calibration plots. |
| **Yansong** | Explainability & Reporting Lead | - Apply SHAP/LIME to interpret feature importance.<br>- Conduct fairness analysis across demographics.<br>- Prepare all visualizations, report sections, and final presentation slides. |

---

## 📝 Team Task Assignment for Proposal

| **Member** | **Main Writing Tasks** | **Supporting Tasks** |
|:--|:--|:--|
| **Binger** | Write **Section 3.A (Data Sources)** and **3.B (Data Preprocessing)**.<br>Provide dataset summary and feature overview. | Contribute EDA figures (class distribution, missing-value map). |
| **Savina** | Write **Section 3.C (Modeling Approach)** and **3.D (Evaluation Metrics)**.<br>Draft baseline modeling descriptions. | Review Abstract & Expected Results for technical clarity. |
| **Yansong** | Write **Abstract, Introduction, Related Work, Expected Results, and Timeline & Roles** sections.<br>Compile and edit full proposal in Overleaf. | Insert SHAP/LIME visuals (concept diagrams) and ensure citation formatting. |

---

## Project Timeline
| Phase | Dates | Deliverables |
|:--|:--|:--|
| Proposal | Nov 1 – Nov 13 | 3-page IEEE-style proposal |
| Modeling | Nov 14 – Nov 27 | Baseline & advanced models |
| Final Report | Nov 28 – Dec 4 | Full report + presentation |

---

## Folder Structure
```text
hospital-readmission-prediction/
│
├── data/
│   ├── raw/                # Original datasets (not committed if large)
│   ├── processed/          # Cleaned/encoded data
│   └── README.md
│
├── notebooks/
│   ├── 01_eda.ipynb        # Student A – data cleaning, EDA
│   ├── 02_modeling.ipynb   # Student B – baseline & advanced models
│   ├── 03_explainability.ipynb  # Student C – SHAP/LIME
│   └── README.md
│
├── src/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── model_evaluation.py
│   └── explainability.py
│
├── results/
│   ├── figures/            # ROC, PR, SHAP plots
│   ├── metrics/            # Model comparison CSVs
│   └── reports/            # Final report drafts
│
├── docs/
│   ├── proposal/           # IEEE proposal (Nov 13)
│   ├── final_report/       # Final report (Dec 4)
│   └── presentation/       # Slides
│
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
