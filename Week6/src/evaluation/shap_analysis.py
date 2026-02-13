import os
import json
import joblib
import shap
import matplotlib.pyplot as plt

from src.features.feature_selector import select_features

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODEL_PATH = os.path.join(BASE_DIR, "models", "best_model.pkl")
EVAL_DIR = os.path.join(BASE_DIR, "evaluation")
os.makedirs(EVAL_DIR, exist_ok=True)


def run_shap():
    X_train, _, y_train, _, feature_names = select_features()

    model = joblib.load(MODEL_PATH)

    explainer = shap.Explainer(model)
    shap_values = explainer(X_train)

    # SHAP Summary Plot
    shap.summary_plot(
        shap_values,
        X_train,
        feature_names=feature_names,
        show=False
    )
    plt.savefig(os.path.join(EVAL_DIR, "shap_summary.png"))
    plt.close()

    # Feature Importance (Global)
    importance = model.feature_importances_

    plt.figure(figsize=(10, 6))
    plt.barh(feature_names, importance)
    plt.title("Feature Importance")
    plt.tight_layout()
    plt.savefig(os.path.join(EVAL_DIR, "feature_importance.png"))
    plt.close()

    print("SHAP analysis completed.")


if __name__ == "__main__":
    run_shap()
