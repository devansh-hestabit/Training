import os
import json
import joblib
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

from xgboost import XGBClassifier
from src.features.feature_selector import select_features


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODELS_DIR = os.path.join(BASE_DIR, "models")
EVAL_DIR = os.path.join(BASE_DIR, "evaluation")

os.makedirs(MODELS_DIR, exist_ok=True)
os.makedirs(EVAL_DIR, exist_ok=True)


def get_models():
    return {
        "logistic_regression": LogisticRegression(
            solver="lbfgs", #lbfgs solver for better performance on small datasets
            C=1.0, #default regularization strength
            max_iter=1000, #increase max iterations to ensure convergence
            random_state=42
        ),

        "random_forest": RandomForestClassifier(
            n_estimators=200,#number of trees in the forest
            max_depth=None,
            random_state=42
        ),
        "xgboost": XGBClassifier(
            n_estimators=200,
            learning_rate=0.1,#step size shrinkage to prevent overfitting
            max_depth=6,
            eval_metric="logloss",#logloss for binary classification
            random_state=42
        ),
        "mlp": MLPClassifier(
            hidden_layer_sizes=(128, 64),
            alpha=0.0001,#L2 regularization
            max_iter=1000,
            random_state=42
        )
    }


def evaluate_model(model, X, y, cv):
    metrics = {
        "accuracy": [],
        "precision": [],
        "recall": [],
        "f1": [],
        "roc_auc": []
    }

    for train_idx, val_idx in cv.split(X, y):
        X_train, X_val = X[train_idx], X[val_idx]
        y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]

        model.fit(X_train, y_train)
        preds = model.predict(X_val)
        probs = model.predict_proba(X_val)[:, 1]

        metrics["accuracy"].append(accuracy_score(y_val, preds))
        metrics["precision"].append(precision_score(y_val, preds))
        metrics["recall"].append(recall_score(y_val, preds))
        metrics["f1"].append(f1_score(y_val, preds))
        metrics["roc_auc"].append(roc_auc_score(y_val, probs))

    return {k: np.mean(v) for k, v in metrics.items()}


def train():
    X_train, X_test, y_train, y_test, feature_names = select_features()

    models = get_models()
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    results = {}
    best_model_name = None
    best_score = 0

    print("\nTraining models with 5-fold cross-validation...\n")

    for name, model in models.items():
        print(f"Training: {name}")
        scores = evaluate_model(model, X_train, y_train, cv)
        results[name] = scores

        print(f"F1 Score: {scores['f1']:.4f}")
        print("-" * 40)

        if scores["f1"] > best_score:
            best_score = scores["f1"]
            best_model_name = name

    print(f"\nBest model selected: {best_model_name}")

    best_model = models[best_model_name]
    best_model.fit(X_train, y_train)

    model_path = os.path.join(MODELS_DIR, "best_model.pkl")
    joblib.dump(best_model, model_path)

    test_preds = best_model.predict(X_test)
    test_probs = best_model.predict_proba(X_test)[:, 1]

    test_metrics = {
        "accuracy": accuracy_score(y_test, test_preds),
        "precision": precision_score(y_test, test_preds),
        "recall": recall_score(y_test, test_preds),
        "f1": f1_score(y_test, test_preds),
        "roc_auc": roc_auc_score(y_test, test_probs)
    }

    results["best_model"] = best_model_name
    results["test_metrics"] = test_metrics


    metrics_path = os.path.join(EVAL_DIR, "metrics.json")
    with open(metrics_path, "w") as f:
        json.dump(results, f, indent=4)


    cm = confusion_matrix(y_test, test_preds)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.title(f"Confusion Matrix - {best_model_name}")
    plt.savefig(os.path.join(EVAL_DIR, "confusion_matrix.png"))
    plt.close()

    print("\nTraining complete.")

if __name__ == "__main__":
    train()
