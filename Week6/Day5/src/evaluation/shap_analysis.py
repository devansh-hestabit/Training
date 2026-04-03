import os
import joblib
import shap
import numpy as np
import matplotlib.pyplot as plt
from Week6.Day5.src.features.feature_selector import select_features
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODEL_PATH = os.path.join(BASE_DIR, "models", "best_model.pkl")
EVAL_DIR = os.path.join(BASE_DIR, "evaluation")
os.makedirs(EVAL_DIR, exist_ok=True)

def run_shap():

    X_train, X_test, y_train, y_test, feature_names = select_features()
    model = joblib.load(MODEL_PATH)
    explainer = shap.Explainer(model)
    shap_values = explainer(X_train)

    shap.summary_plot(
        shap_values,
        X_train,
        feature_names=feature_names,
        show=False
    )
    plt.tight_layout()
    plt.savefig(os.path.join(EVAL_DIR, "shap_summary.png"))
    plt.close()

    importance = model.feature_importances_
    plt.figure(figsize=(10, 6))
    plt.barh(feature_names, importance)
    plt.title("Feature Importance")
    plt.tight_layout()
    plt.savefig(os.path.join(EVAL_DIR, "feature_importance.png"))
    plt.close()


    y_pred = model.predict(X_test)
    errors = y_pred - y_test
    abs_errors = np.abs(errors)

    print("MAE:", abs_errors.mean())
    print("Max error:", abs_errors.max())
    print("Non-zero errors:", np.count_nonzero(abs_errors))
    print("Total samples:", len(abs_errors))

    plt.figure(figsize=(8, 6))
    plt.hist2d(
        y_test,
        np.abs(y_pred - y_test),
        bins=20,
        cmap="magma"
    )
    
    plt.colorbar(label="Number of Samples")
    plt.xlabel("True Values")
    plt.ylabel("Absolute Error")
    plt.title("Error Magnitude Heatmap")
    
    plt.tight_layout()
    plt.savefig(os.path.join(EVAL_DIR, "error_magnitude_heatmap.png"))
    plt.close()



if __name__ == "__main__":
    run_shap()
