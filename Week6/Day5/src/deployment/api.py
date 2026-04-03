import os
import uuid #for generating unique request IDs
from datetime import datetime

import joblib
import pandas as pd
from fastapi import FastAPI #for building the API 
from pydantic import BaseModel  #for defining data models for request and response validation

from Week6.Day5.src.features.build_features import create_new_features
app = FastAPI(title="Income Prediction API")

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

MODEL_PATH = os.path.join(BASE_DIR, "models", "best_model.pkl")
PREPROCESSOR_PATH = os.path.join(BASE_DIR, "models", "preprocessor.pkl")
SELECTOR_PATH = os.path.join(BASE_DIR, "models", "selector.pkl")
LOG_PATH = os.path.join(BASE_DIR, "prediction_logs.csv")
model = joblib.load(MODEL_PATH)
preprocessor = joblib.load(PREPROCESSOR_PATH)
selector = joblib.load(SELECTOR_PATH)

#input schema
class PredictionInput(BaseModel):
    age: int
    education_num: int
    hours_per_week: int
    capital_gain: int
    capital_loss: int
    sex: str
    marital_status: str
    education: str
    occupation: str
    relationship: str
    workclass: str
    race: str
    native_country: str

class PredictionOutput(BaseModel):
    request_id: str
    prediction: int
    probability: float
    model_version: str
    timestamp: str


@app.post("/predict", response_model=PredictionOutput)
def predict(data: PredictionInput):

    request_id = str(uuid.uuid4())
    timestamp = datetime.now().isoformat()

    raw_df = pd.DataFrame([{
    "age": data.age,
    "education.num": data.education_num,
    "hours.per.week": data.hours_per_week,
    "capital.gain": data.capital_gain,
    "capital.loss": data.capital_loss,
    "sex": data.sex,
    "marital.status": data.marital_status,
    "education": data.education,
    "occupation": data.occupation,
    "relationship": data.relationship,
    "workclass": data.workclass,
    "race": data.race,
    "native.country": data.native_country
}])

    engineered_df = create_new_features(raw_df)
    X_processed = preprocessor.transform(engineered_df)
    X_selected = selector.transform(X_processed)
    prob = model.predict_proba(X_selected)[0][1]
    prediction = int(prob >= 0.5)
    
    log_row = {
    "request_id": request_id,
    "timestamp": timestamp,
    "prediction": prediction,
    "probability": float(prob),
    "model_version": "xgboost_v1"
    }

    log_df = pd.DataFrame([log_row])

    if os.path.exists(LOG_PATH):
        log_df.to_csv(LOG_PATH, mode="a", header=False, index=False)
    else:
        log_df.to_csv(LOG_PATH, index=False)


    return PredictionOutput(
        request_id=request_id,
        prediction=prediction,  
        probability=round(prob, 4),
        model_version="xgboost_v1",
        timestamp=timestamp
    )
