# Cardiac Patient Monitoring System — Findings & Limitations

## Dataset
- 303 patients, 13 features, UCI Cleveland Heart Disease database.
- Target binarized: 164 absence (54.1%) / 139 presence (45.9%).
- 6 missing values total (ca: 4, thal: 2); no duplicates; no invalid values.

## Supervised Learning Results
|                     |   accuracy |   precision |   recall |     f1 |   roc_auc |   cv_f1_mean |   cv_f1_std |
|:--------------------|-----------:|------------:|---------:|-------:|----------:|-------------:|------------:|
| Logistic Regression |     0.8689 |      0.8125 |   0.9286 | 0.8667 |    0.9578 |       0.8254 |      0.015  |
| Random Forest       |     0.9016 |      0.8438 |   0.9643 | 0.9    |    0.9545 |       0.7917 |      0.0374 |

## After Feature Engineering
|                           |   accuracy |   precision |   recall |     f1 |   roc_auc |
|:--------------------------|-----------:|------------:|---------:|-------:|----------:|
| Logistic Regression (+FE) |     0.8689 |      0.8125 |   0.9286 | 0.8667 |    0.9578 |
| Random Forest (+FE)       |     0.8852 |      0.8387 |   0.9286 | 0.8814 |    0.9556 |

## Model Conclusion
Random Forest selected as the final pipeline artifact for consistently higher recall
(0.929-0.964), the priority metric given this project's medical framing (false negatives are
costlier than false positives), while Logistic Regression showed more stable cross-validation
performance (lower std) as an explicit caveat.

## Unsupervised Learning
K-Means (k=2, chosen via elbow + silhouette) produced clusters with 77.1% vs 22.1% disease-presence
proportions -- a meaningful post-hoc alignment with the known target, though the clusters were
formed without using the target. Silhouette score was modest (~0.175).

## Key Limitations
- Small sample size (303 rows, 61-row test set) -- metrics carry real uncertainty.
- Single-source, single-era data (Cleveland only, ~1988) -- limited generalizability.
- ~68% male demographic imbalance in source data.
- Feature engineering did not improve results in this run.
- Educational project only -- not a clinical diagnostic tool.
