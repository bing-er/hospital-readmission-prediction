# 🏥 Predicting Hospital Readmissions Using Public Health Data

## Overview
This project aims to predict 30-day hospital readmissions using the UCI Diabetes 130-Hospital dataset. We compare traditional ML models (Logistic Regression, Random Forest) and ensemble models (XGBoost) with explainability tools such as SHAP and LIME.

## Team Members
- **Student B** – Data Engineer / Preprocessing Lead  
- **Student S** – Modeling & Evaluation Lead  
- **Student Y** – Explainability & Reporting Lead  

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
