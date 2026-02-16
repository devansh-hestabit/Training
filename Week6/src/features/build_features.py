import os
import json
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
import joblib

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "final.csv")

TARGET_COL = "income"

def load_data():
    return pd.read_csv(DATA_PATH)


def create_new_features(df):
    df = df.copy()
    if "fnlwgt" in df.columns:
        df = df.drop(columns=["fnlwgt"])

    original_cols = df.columns.tolist()

    df["has_capital_gain"] = (df["capital.gain"] > 0).astype(int)
    df["has_capital_loss"] = (df["capital.loss"] > 0).astype(int)
    df["capital_total"] = df["capital.gain"] + df["capital.loss"]
    df["capital_per_hour"] = df["capital_total"] / (df["hours.per.week"] + 1)

    df["age_squared"] = df["age"] ** 2
    df["age_education_interaction"] = df["age"] * df["education.num"]
    df["education_hours_interaction"] = df["education.num"] * df["hours.per.week"]

    df["high_work_hours"] = (df["hours.per.week"] > 0).astype(int)
    df["advanced_education"] = (df["education.num"] > 0).astype(int)

    df["age_group"] = pd.cut(
        df["age"],
        bins=[-np.inf, -0.5, 0.5, np.inf],
        labels=["young", "middle", "senior"]
    )
    return df


def run():

    df = load_data()
    df = create_new_features(df)

    y = df[TARGET_COL].map({"<=50K": 0, ">50K": 1})
    X = df.drop(columns=[TARGET_COL])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    categorical_cols = X.select_dtypes(include=["object", "category","string"]).columns
    numerical_cols = X.select_dtypes(include=["number"]).columns

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numerical_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_cols)
        ]
    )

    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)
    feature_names = preprocessor.get_feature_names_out()
    feature_path = os.path.join(BASE_DIR, "features", "feature_list.json")

    os.makedirs(os.path.dirname(feature_path), exist_ok=True)

    with open(feature_path, "w") as f:
        json.dump(list(feature_names), f, indent=4)

    PREPROCESSOR_PATH = os.path.join(BASE_DIR, "models", "preprocessor.pkl")

    joblib.dump(preprocessor, PREPROCESSOR_PATH)

    print("Feature pipeline completed.")

    return X_train_processed, X_test_processed, y_train, y_test, feature_names

if __name__ == "__main__":
    run()
