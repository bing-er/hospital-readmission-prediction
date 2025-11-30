"""
Data preprocessing pipeline for the UCI Diabetes 130-US Hospitals dataset.

Student A – Data Engineer / Preprocessing Lead:
- Load raw data from data/raw/
- Clean missing values, drop ID columns
- Handle invalid entries
- Encode target variable (readmitted -> readmitted_binary)
- Feature engineering (age_mid, service_utilization)
- Save cleaned dataset to data/processed/diabetes_cleaned.csv
"""

from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pandas as pd


# --------------------------------------------------------------------
# Paths (Corrected for robust execution)
# --------------------------------------------------------------------
# Define the root as the parent directory of the script's location
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

# Use the project root to define relative paths for data files
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "diabetic_data.csv"
PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed" / "diabetes_cleaned.csv"

# --------------------------------------------------------------------
# Helper functions
# --------------------------------------------------------------------
def age_to_midpoint(value: str) -> float | np.nan:
    """
    Convert an age range string to a numeric midpoint.

    Handles forms like:
      "[50-60)" or "50-60"
    Returns NaN if it cannot parse.
    """
    if pd.isna(value):
        return np.nan

    s = str(value).strip()
    # Remove brackets and spaces: "[50-60)" -> "50-60"
    s = s.replace("[", "").replace(")", "").replace(" ", "")

    m = re.match(r"(\d+)-(\d+)", s)
    if not m:
        return np.nan

    low, high = map(int, m.groups())
    return (low + high) / 2.0


def load_raw_data(path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """Load the raw UCI diabetes dataset."""
    if not path.exists():
        # Fallback to current directory if structured path fails
        local_path = Path("diabetic_data.csv")
        if local_path.exists():
             path = local_path
        else:
             raise FileNotFoundError(f"Raw data file not found at expected location: {path}")

    df = pd.read_csv(path)
    print(f"[load_raw_data] Loaded raw data with shape: {df.shape}")
    return df

def clean_diabetes_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # 1) Missing markers
    df.replace(to_replace="?", value=np.nan, inplace=True)

    # 2) Drop columns with excessive missingness or not useful
    cols_to_drop = [
        "weight",
        "payer_code",
        "medical_specialty",
        "A1Cresult",        # Dropped for sparsity
        "max_glu_serum",    # Dropped for sparsity
        "encounter_id",
        "patient_nbr",
    ]
    df.drop(columns=[c for c in cols_to_drop if c in df.columns], inplace=True)

    # 3) Drop invalid gender rows
    if "gender" in df.columns:
        df = df[df["gender"] != "Unknown/Invalid"].copy()

    # 4) Encode target: readmitted_binary
    readmit_map = {"<30": 1, ">30": 0, "NO": 0}
    df["readmitted_binary"] = df["readmitted"].map(readmit_map).astype("int8")

    # 5) Convert age ranges to midpoints
    age_mid_map = {
        "[0-10)": 5, "[10-20)": 15, "[20-30)": 25, "[30-40)": 35,
        "[40-50)": 45, "[50-60)": 55, "[60-70)": 65, "[70-80)": 75,
        "[80-90)": 85, "[90-100)": 95,
    }
    df["age_mid"] = df["age"].map(age_mid_map).astype("int64")

    # 6) Create service utilization feature
    df["service_utilization"] = (
        df["number_outpatient"]
        + df["number_emergency"]
        + df["number_inpatient"]
    )

    print(f"[clean_diabetes_data] Finished cleaning. New shape: {df.shape}")
    return df


def save_clean_data(df: pd.DataFrame, path: Path = PROCESSED_DATA_PATH) -> None:
    """Save the cleaned DataFrame to CSV."""
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    print(f"[save_clean_data] Saved cleaned data to: {path}")


# --------------------------------------------------------------------
# Main entry point
# --------------------------------------------------------------------
def main() -> None:
    """Run the full preprocessing pipeline."""
    print("[main] Starting preprocessing pipeline...")
    df_raw = load_raw_data()
    df_clean = clean_diabetes_data(df_raw)
    save_clean_data(df_clean)

    # Sanity check: print column count and a sample
    print(f"[main] Cleaned data shape: {df_clean.shape}")
    print("[main] First 5 columns:", list(df_clean.columns[:5]))
    print(df_clean.head(3))


if __name__ == "__main__":
    main()