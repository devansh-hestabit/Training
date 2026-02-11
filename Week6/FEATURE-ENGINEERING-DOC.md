#  Feature Engineering & Feature Selection

## Data Preprocessing (Day 1)

Operations performed:

-   Replace "?" with NaN
-   Fill numeric missing values using median
-   Fill categorical missing values using mode
-   Remove duplicate rows
-   Remove outliers using IQR method (excluding capital.gain and
    capital.loss)
-   Save cleaned dataset as `final.csv`


## Feature Engineering

Engineered Features Created:

-   has_capital_gain
-   has_capital_loss
-   capital_total
-   capital_per_hour
-   age_squared
-   age_education_interaction
-   education_hours_interaction
-   high_work_hours
-   advanced_education
-   age_group


## Encoding & Scaling

Numerical Features: - StandardScaler applied 
Categorical Features: - OneHotEncoder used 
ColumnTransformer ensures: - No data leakage - Train-only fitting -

## Train/Test Split

-   test_size=0.2
-   random_state=42 (reproducibility)
-   stratify=y (class balance maintained)


## Feature Selection

Technique used:

Mutual Information- It is a non-parametric method that measures the dependency between each feature and the target variable. It captures both linear and non-linear relationships, making it suitable for our dataset.

SelectKBest(score_func=mutual_info_classif, k=20)

## Key Insights 

- Scaling before train/test split causes data leakage.
- `.fit()` must be done only on training data.
- Encoding train and test separately breaks feature alignment.
- OneHot encoding significantly increases dimensionality.
- `handle_unknown="ignore"` prevents production failures.
- `ColumnTransformer` avoids manual preprocessing errors.
- Stratified split preserves class balance.
- `random_state` ensures reproducibility.
