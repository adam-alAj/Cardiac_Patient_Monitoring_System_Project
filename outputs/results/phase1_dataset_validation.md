# Phase 1 — Dataset Validation Report

## Dataset

UCI Heart Disease — Cleveland Database

## Official Source

UCI Machine Learning Repository

https://archive.ics.uci.edu/dataset/45/heart+disease

DOI:

10.24432/C52P4X

## Dataset Structure

- Observations: 303
- Features: 13
- Target: num
- Task: Classification
- Feature types: Categorical, Integer, Real

## Features

1. age
2. sex
3. cp
4. trestbps
5. chol
6. fbs
7. restecg
8. thalach
9. exang
10. oldpeak
11. slope
12. ca
13. thal

## Missing Values

| Feature | Missing Values |
|---|---:|
| ca | 4 |
| thal | 2 |

Total missing feature values: 6

## Target Distribution

| Target | Count |
|---:|---:|
| 0 | 164 |
| 1 | 55 |
| 2 | 36 |
| 3 | 35 |
| 4 | 13 |

Total observations: 303

## Initial Validation Conclusion

The dataset was successfully retrieved from the official UCI
Machine Learning Repository.

The dataset contains 303 observations and 13 features.
Missing values are present in `ca` and `thal`.

The original target `num` contains five integer classes:
0, 1, 2, 3, and 4.

No preprocessing or target transformation was performed during
the initial validation stage.

The raw dataset will be preserved unchanged for subsequent phases.
