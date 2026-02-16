# MLOps Debugging & Issues Log — Week 6 Capstone


## 1. Python Module Import Errors

**Error**
ModuleNotFoundError: No module named 'features', 'deployment', or 'src'

**Cause**
Scripts were executed directly instead of as modules, so Python could not resolve package paths.

**Fix**
Run using module syntax:
python -m src.training.train
python -m uvicorn src.deployment.api:app --reload

**Lesson**
Always structure ML projects as Python packages.


## 2. Model Always Predicting 0

**Cause**
Inference pipeline did not match training pipeline (feature engineering and selection mismatch).

**Fix**
Reuse the same feature engineering, preprocessing, and feature selection logic at inference time.

**Lesson**
Training and inference pipelines must be identical.


## 3. Preprocessor / Selector Pickle Failures

**Error**
StringDtype errors and pandas NotImplementedError.

**Cause**
Pickled preprocessing objects were incompatible across pandas/sklearn versions.

**Fix**
Rebuild preprocessing and feature selection inside api.py instead of loading pickles.

**Lesson**
Never pickle pandas or sklearn preprocessing pipelines for production.


## 4. Missing Columns at Inference

**Error**
ValueError: columns are missing

**Cause**
API expected raw features but received incomplete input.

**Fix**
Define a strict input schema and accept only raw features; perform feature engineering internally.

**Lesson**
APIs must always accept raw user inputs.


## 5. Docker Dependency Failures

**Cause**
Using pip freeze from dev environment introduced incompatible packages.

**Fix**
Create a minimal requirements.prod.txt with only inference dependencies.

**Lesson**
Never deploy using full pip freeze in ML projects.


## 6. Pickle Compatibility Errors in Docker

**Cause**
Mismatch between Python and pandas versions used for training and deployment.

**Fix**
Align Python versions and avoid pickling preprocessing objects.

