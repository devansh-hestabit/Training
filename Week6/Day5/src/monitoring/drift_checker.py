import pandas as pd
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOG_PATH = os.path.join(BASE_DIR, "prediction_logs.csv")

def check_drift():

    if not os.path.exists(LOG_PATH):
        print("No prediction logs found.")
        return

    df = pd.read_csv(LOG_PATH)

    if df.empty:
        print("Prediction log is empty.")
        return
    df["prediction"] = pd.to_numeric(df["prediction"], errors="coerce") #convert to numeric, coerce errors to NaN
    df["probability"] = pd.to_numeric(df["probability"], errors="coerce")

    df = df.dropna(subset=["prediction", "probability"])

    if df.empty:
        print("No valid prediction data available.")
        return

    mean_prob = df["probability"].mean()
    positive_rate = df["prediction"].mean()

    print(f"Average prediction probability: {mean_prob:.4f}")
    print(f"Positive class rate: {positive_rate:.4f}")

    if mean_prob < 0.2 or mean_prob > 0.8:
        print("Prediction confidence drift detected.")

    if positive_rate < 0.1 or positive_rate > 0.9:
        print("Class distribution drift detected.")

    print("\nDrift check completed.")

if __name__ == "__main__":
    check_drift()
