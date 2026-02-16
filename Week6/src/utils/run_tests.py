

import requests
import json

API_URL = "http://127.0.0.1:8000/predict"

test_cases = [
    {
        "age": 48,
        "education_num": 16,
        "hours_per_week": 55,
        "capital_gain": 20000,
        "capital_loss": 0,
        "sex": "Male",
        "marital_status": "Married-civ-spouse",
        "education": "Masters",
        "occupation": "Exec-managerial",
        "relationship": "Husband",
        "workclass": "Private",
        "race": "White",
        "native_country": "United-States"
    },
    {
        "age": 23,
        "education_num": 9,
        "hours_per_week": 20,
        "capital_gain": 0,
        "capital_loss": 0,
        "sex": "Female",
        "marital_status": "Never-married",
        "education": "HS-grad",
        "occupation": "Other-service",
        "relationship": "Not-in-family",
        "workclass": "Private",
        "race": "Black",
        "native_country": "United-States"
    },
    {
        "age": 35,
        "education_num": 13,
        "hours_per_week": 40,
        "capital_gain": 0,
        "capital_loss": 0,
        "sex": "Male",
        "marital_status": "Never-married",
        "education": "Bachelors",
        "occupation": "Sales",
        "relationship": "Not-in-family",
        "workclass": "Private",
        "race": "White",
        "native_country": "United-States"
    },
    {
        "age": 42,
        "education_num": 10,
        "hours_per_week": 48,
        "capital_gain": 0,
        "capital_loss": 0,
        "sex": "Male",
        "marital_status": "Married-civ-spouse",
        "education": "Some-college",
        "occupation": "Craft-repair",
        "relationship": "Husband",
        "workclass": "Private",
        "race": "White",
        "native_country": "United-States"
    },
    {
        "age": 39,
        "education_num": 14,
        "hours_per_week": 50,
        "capital_gain": 5000,
        "capital_loss": 0,
        "sex": "Female",
        "marital_status": "Married-civ-spouse",
        "education": "Masters",
        "occupation": "Prof-specialty",
        "relationship": "Wife",
        "workclass": "Private",
        "race": "Asian-Pac-Islander",
        "native_country": "India"
    }
]

for i, case in enumerate(test_cases, 1):
    print(f"\n===== Test Case {i} =====")
    response = requests.post(API_URL, json=case)
    try:
        print(json.dumps(response.json(), indent=2))
    except Exception:
        print(response.text)
