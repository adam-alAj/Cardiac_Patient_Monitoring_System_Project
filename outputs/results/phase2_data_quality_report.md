# Phase 2 — Data Cleaning & Data Quality Report
- Rows: 303, Columns: 15
## Missing values
- `ca`: 4 missing (1.32%) -> planned median imputation (fit on train only)
- `thal`: 2 missing (0.66%) -> planned mode imputation (fit on train only)
## Duplicates
- Fully duplicated rows: 0 (none removed)
## Invalid values
- All categorical columns within documented value sets. None found.
## Data types
- Numerical: ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
- Categorical: ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']
- Target (binary, derived): target; Raw target (preserved): num
## Outliers (IQR screening, numerical features)
- age: 0 flagged points (kept, not removed)
- trestbps: 9 flagged points (kept, not removed)
- chol: 5 flagged points (kept, not removed)
- thalach: 1 flagged points (kept, not removed)
- oldpeak: 5 flagged points (kept, not removed)
## Target class balance
- absence (0): 164
- presence (1): 139
