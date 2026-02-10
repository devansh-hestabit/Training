import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Base directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "dataset.csv")
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "final.csv")


def load_data(path):
    print("Loading raw dataset...")
    df = pd.read_csv(path)
    return df


def handle_missing_values(df):
    print("Handling missing values...")

    # Replace '?' with NaN
    df.replace("?", np.nan, inplace=True)

    # Numerical columns → median
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    # Categorical columns → mode
    categorical_cols = df.select_dtypes(include=["object", "string"]).columns
    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    return df


def remove_duplicates(df):
    print("Removing duplicate rows...")
    return df.drop_duplicates()


OUTLIER_EXCLUDE_COLS = ["capital.gain", "capital.loss"]

def remove_outliers(df):
    print("Removing outliers (IQR method)...")

    numeric_cols = df.select_dtypes(include=[np.number]).columns
    numeric_cols = [col for col in numeric_cols if col not in OUTLIER_EXCLUDE_COLS]

    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        df = df[(df[col] >= lower) & (df[col] <= upper)]

    return df



def scale_numeric_features(df):
    print("Scaling numerical features...")

    scaler = StandardScaler()
    numeric_cols = df.select_dtypes(include=[np.number]).columns

    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df


def save_processed_data(df, path):
    print("Saving processed dataset...")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)


def run_pipeline():
    df = load_data(RAW_DATA_PATH)
    df = handle_missing_values(df)
    df = remove_duplicates(df)
    df = remove_outliers(df)
    df = scale_numeric_features(df)
    save_processed_data(df, PROCESSED_DATA_PATH)

    print("Data Pipeline Completed Successfully!")


if __name__ == "__main__":
    run_pipeline()
