import os
import json
import joblib
import optuna
import numpy as np

from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score, roc_auc_score
from xgboost import XGBClassifier

from src.features.feature_selector import select_features

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TUNING_DIR = os.path.join(BASE_DIR, "tuning")
MODELS_DIR = os.path.join(BASE_DIR, "models")
EVAL_DIR = os.path.join(BASE_DIR, "evaluation")

os.makedirs(TUNING_DIR, exist_ok=True)
os.makedirs(MODELS_DIR, exist_ok=True)
os.makedirs(EVAL_DIR, exist_ok=True)


def objective(trial):
    X_train, _, y_train, _, _ = select_features()

    params = {
        "n_estimators": trial.suggest_int("n_estimators", 150, 400),
        "max_depth": trial.suggest_int("max_depth", 3, 8),
        "learning_rate": trial.suggest_float("learning_rate", 0.01, 0.2),
        "subsample": trial.suggest_float("subsample", 0.7, 1.0),
        "colsample_bytree": trial.suggest_float("colsample_bytree", 0.7, 1.0),
        "eval_metric": "logloss",
        "random_state": 42
    }

    model = XGBClassifier(**params)

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scores = []

    for train_idx, val_idx in cv.split(X_train, y_train):
        X_tr, X_val = X_train[train_idx], X_train[val_idx]
        y_tr, y_val = y_train.iloc[train_idx], y_train.iloc[val_idx]

        model.fit(X_tr, y_tr)
        preds = model.predict(X_val)
        scores.append(f1_score(y_val, preds))

    return np.mean(scores)


def run_tuning():
    print("Starting hyperparameter tuning...")

    study = optuna.create_study(direction="maximize")
    study.optimize(objective, n_trials=15)

    print("Tuning completed.")
    print("Best F1 Score:", study.best_value)
    print("Best Parameters:", study.best_params)

    X_train, X_test, y_train, y_test, _ = select_features()

    best_model = XGBClassifier(
        **study.best_params,
        eval_metric="logloss",
        random_state=42
    )

    best_model.fit(X_train, y_train)

    test_preds = best_model.predict(X_test)
    test_probs = best_model.predict_proba(X_test)[:, 1]

    test_metrics = {
        "accuracy": accuracy_score(y_test, test_preds),
        "precision": precision_score(y_test, test_preds),
        "recall": recall_score(y_test, test_preds),
        "f1": f1_score(y_test, test_preds),
        "roc_auc": roc_auc_score(y_test, test_probs)
    }

    model_path = os.path.join(MODELS_DIR, "best_model.pkl")
    joblib.dump(best_model, model_path)
    tuning_results = {
        "best_cv_f1": study.best_value,
        "best_params": study.best_params,
        "test_metrics_after_tuning": test_metrics,
    }

    with open(os.path.join(TUNING_DIR, "results.json"), "w") as f:
        json.dump(tuning_results, f, indent=4)

    print("Tuned model saved and replaced best_model.pkl")
    print("Tuning results saved to /tuning/results.json")


if __name__ == "__main__":
    run_tuning()
