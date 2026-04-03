import os
import pandas as pd
import numpy as np

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "dataset.csv")
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "final.csv")


def load_data(path):
    return pd.read_csv(path)


def handle_missing_values(df):
    df = df.replace("?", np.nan)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())#fill missing numeric values with median

    categorical_cols = df.select_dtypes(include=["object", "string"]).columns
    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0]) #fill missing categorical values with most frequent category

    return df


def remove_duplicates(df):
    return df.drop_duplicates()


def remove_outliers(df):
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    numeric_cols = [col for col in numeric_cols if col not in ["capital.gain", "capital.loss"]] #exclude capital.gain and capital.loss from outlier removal since they have many zeros and few large values which are valid

    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        df = df[(df[col] >= lower) & (df[col] <= upper)]

    return df


def run_pipeline():
    df = load_data(RAW_DATA_PATH)
    df = handle_missing_values(df)
    df = remove_duplicates(df)
    df = remove_outliers(df)

    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)



if __name__ == "__main__":
    run_pipeline()
