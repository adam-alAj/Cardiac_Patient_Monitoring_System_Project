# Heart Disease Cleveland Dataset — Data Dictionary

## 1. Dataset Information

| Property | Value |
|---|---|
| Dataset | Heart Disease |
| Database | Cleveland |
| UCI Dataset ID | 45 |
| Repository | UCI Machine Learning Repository |
| Official Source | https://archive.ics.uci.edu/dataset/45/heart+disease |
| DOI | 10.24432/C52P4X |
| Task | Classification |
| Observations | 303 |
| Features | 13 |
| Target | num |
| Feature Types | Categorical, Integer, Real |
| Missing Values | Yes |
| Missing Value Symbol | NaN |
| Dataset Creation Year | 1989 |
| Last Updated | November 3, 2023 |

---

## 2. Dataset Retrieval

The dataset was retrieved programmatically from the UCI Machine Learning Repository using the `ucimlrepo` Python package.

The UCI dataset identifier used for retrieval was:

45

The retrieved feature matrix has:

- 303 observations
- 13 features

The retrieved target contains:

- 303 observations
- 1 target column

The raw dataset retrieved from UCI is stored locally at:

data/raw/heart_disease_cleveland_raw.csv

---

## 3. Official Source

UCI Machine Learning Repository:

https://archive.ics.uci.edu/dataset/45/heart+disease

Dataset DOI:

10.24432/C52P4X

The dataset metadata identifies the task as classification and describes the dataset as multivariate, with categorical, integer, and real-valued feature types.

---

## 4. Features

| Feature | Data Type | Role | Description | Units | Missing |
|---|---|---|---|---|---|
| age | Integer | Feature | Age of the patient | years | No |
| sex | Categorical | Feature | Sex of the patient | — | No |
| cp | Categorical | Feature | Chest pain type | — | No |
| trestbps | Integer | Feature | Resting blood pressure on admission | mm Hg | No |
| chol | Integer | Feature | Serum cholesterol | mg/dl | No |
| fbs | Categorical | Feature | Fasting blood sugar > 120 mg/dl | — | No |
| restecg | Categorical | Feature | Resting electrocardiographic results | — | No |
| thalach | Integer | Feature | Maximum heart rate achieved | — | No |
| exang | Categorical | Feature | Exercise-induced angina | — | No |
| oldpeak | Real/Numeric | Feature | ST depression induced by exercise relative to rest | — | No |
| slope | Categorical | Feature | Slope of the peak exercise ST segment | — | No |
| ca | Integer | Feature | Number of major vessels colored by fluoroscopy | vessels | Yes |
| thal | Categorical | Feature | Thallium test result | — | Yes |
| num | Integer | Target | Diagnosis of heart disease / angiographic disease status | — | No |

---

## 5. Detailed Feature Definitions

### 5.1 age

Patient age in years.

Data type:

Integer

Observed range in the retrieved dataset:

29–77

---

### 5.2 sex

Sex of the patient.

Values:

0 = female

1 = male

Data type:

Categorical

---

### 5.3 cp

Chest pain type.

Values:

1 = typical angina

2 = atypical angina

3 = non-anginal pain

4 = asymptomatic

Data type:

Categorical

---

### 5.4 trestbps

Resting blood pressure measured on admission to the hospital.

Unit:

mm Hg

Data type:

Integer

Observed range in the retrieved dataset:

94–200

---

### 5.5 chol

Serum cholesterol.

Unit:

mg/dl

Data type:

Integer

Observed range in the retrieved dataset:

126–564

---

### 5.6 fbs

Fasting blood sugar greater than 120 mg/dl.

Values:

0 = false

1 = true

Data type:

Categorical

---

### 5.7 restecg

Resting electrocardiographic results.

Values:

0 = normal

1 = ST-T wave abnormality

2 = probable or definite left ventricular hypertrophy according to Estes' criteria

Data type:

Categorical

---

### 5.8 thalach

Maximum heart rate achieved.

Data type:

Integer

Observed range in the retrieved dataset:

71–202

---

### 5.9 exang

Exercise-induced angina.

Values:

0 = no

1 = yes

Data type:

Categorical

---

### 5.10 oldpeak

ST depression induced by exercise relative to rest.

Data type:

Real/Numeric

Observed range in the retrieved dataset:

0.0–6.2

---

### 5.11 slope

Slope of the peak exercise ST segment.

Values:

1 = upsloping

2 = flat

3 = downsloping

Data type:

Categorical

---

### 5.12 ca

Number of major vessels colored by fluoroscopy.

Expected values:

0–3

Data type:

Integer

Missing values:

4

Observed non-missing range in the retrieved dataset:

0–3

---

### 5.13 thal

Thallium test result.

Values:

3 = normal

6 = fixed defect

7 = reversible defect

Data type:

Categorical

Missing values:

2

---

## 6. Target Variable

The original target variable is:

num

Data type:

Integer

Role:

Target

The retrieved dataset contains five original target classes:

0

1

2

3

4

The observed distribution is:

| Original Target | Meaning | Count |
|---:|---|---:|
| 0 | Absence of heart disease | 164 |
| 1 | Presence of heart disease | 55 |
| 2 | Presence of heart disease | 36 |
| 3 | Presence of heart disease | 35 |
| 4 | Presence of heart disease | 13 |
| Total | — | 303 |

The UCI documentation states that experiments with the Cleveland database have concentrated on distinguishing absence (value 0) from presence (values 1, 2, 3, and 4).

---

## 7. Planned Binary Target Transformation

For the supervised binary classification stage, the original target will be transformed into a binary target.

Transformation:

0 → 0

1 → 1

2 → 1

3 → 1

4 → 1

Interpretation:

0 = absence of heart disease

1 = presence of heart disease

The original `num` variable must be preserved in the raw dataset.

The binary target transformation must only be performed on a processed/derived dataset during the appropriate preprocessing stage.

The transformation must be documented in the project and must not overwrite the original target in the raw data.

---

## 8. Missing Values

Missing values were detected in two feature columns.

| Feature | Missing Count | Missing Percentage |
|---|---:|---:|
| ca | 4 | 1.32% |
| thal | 2 | 0.66% |
| Total | 6 | 1.98% |

No missing values were detected in the target variable.

The missing values will not be manually replaced during the validation stage.

A formal missing-value handling strategy will be selected during the data-cleaning/preprocessing phase.

---

## 9. Observed Dataset Statistics

| Feature | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| age | 303 | 54.4389 | 9.0387 | 29 | 48 | 56 | 61 | 77 |
| sex | 303 | 0.6799 | 0.4673 | 0 | 0 | 1 | 1 | 1 |
| cp | 303 | 3.1584 | 0.9601 | 1 | 3 | 3 | 4 | 4 |
| trestbps | 303 | 131.6898 | 17.5997 | 94 | 120 | 130 | 140 | 200 |
| chol | 303 | 246.6931 | 51.7769 | 126 | 211 | 241 | 275 | 564 |
| fbs | 303 | 0.1485 | 0.3562 | 0 | 0 | 0 | 0 | 1 |
| restecg | 303 | 0.9901 | 0.9950 | 0 | 0 | 1 | 2 | 2 |
| thalach | 303 | 149.6073 | 22.8750 | 71 | 133.5 | 153 | 166 | 202 |
| exang | 303 | 0.3267 | 0.4698 | 0 | 0 | 0 | 1 | 1 |
| oldpeak | 303 | 1.0396 | 1.1611 | 0.0 | 0.0 | 0.8 | 1.6 | 6.2 |
| slope | 303 | 1.6007 | 0.6162 | 1 | 1 | 2 | 2 | 3 |
| ca | 299 | 0.6722 | 0.9374 | 0 | 0 | 0 | 1 | 3 |
| thal | 301 | 4.7342 | 1.9397 | 3 | 3 | 3 | 7 | 7 |

Note:

The statistics above describe the retrieved raw dataset before preprocessing, imputation, encoding, scaling, feature engineering, or outlier treatment.

---

## 10. Dataset Quality Findings From Initial Validation

The initial validation identified the following:

1. The dataset contains 303 observations.
2. The dataset contains 13 predictor features.
3. The target variable is `num`.
4. The target contains five original classes.
5. Six missing feature values were detected.
6. Missing values occur only in `ca` and `thal`.
7. The target variable contains no missing values.
8. The dataset contains both categorical and numerical variables.
9. The dataset is therefore suitable for demonstrating mixed-type preprocessing.
10. The dataset is suitable for binary classification after the documented target transformation.
11. The original raw data must remain unchanged.

---

## 11. Raw Data Preservation

The original retrieved dataset is stored at:

data/raw/heart_disease_cleveland_raw.csv

This file represents the raw input data and must remain unchanged.

No imputation, encoding, scaling, normalization, feature engineering, outlier removal, or target transformation should be performed directly on this file.

All transformations must be applied to derived data in:

data/processed/

---

## 12. Reproducibility

The dataset was retrieved programmatically using:

`ucimlrepo`

UCI dataset identifier:

45

The retrieval process is documented in:

notebooks/01_dataset_validation.ipynb

The raw retrieved data is stored in:

data/raw/heart_disease_cleveland_raw.csv

The validation results are documented in:

outputs/results/phase1_dataset_validation.md

---

## 13. Dataset Scope

The project uses the Cleveland database represented by the retrieved 303-row dataset.

Although the UCI Heart Disease repository contains information related to multiple databases, the current project does not combine Cleveland with the Hungary, Switzerland, or VA Long Beach datasets.

Only the retrieved Cleveland dataset is used for the project.

---

## 14. Privacy and Identification

According to the UCI dataset documentation, patient names and social security numbers were removed from the database and replaced with dummy values.

The project does not use direct patient identifiers as modeling features.

No additional personally identifying information will be introduced into the project dataset.

---

## 15. Important Data Handling Rules

The following rules apply throughout the project:

1. Never modify the raw CSV.
2. Never overwrite the original `num` target.
3. Perform train/test splitting before fitting preprocessing components where applicable.
4. Fit imputers, scalers, encoders, and other learned preprocessing components only on training data.
5. Use pipelines where appropriate to reduce data leakage risk.
6. Document every transformation applied to the dataset.
7. Keep processed datasets separate from raw data.
8. Preserve reproducibility by recording dependencies and preprocessing decisions.

---

## 16. Source Reference

UCI Machine Learning Repository — Heart Disease:

https://archive.ics.uci.edu/dataset/45/heart+disease

Dataset DOI:

10.24432/C52P4X
