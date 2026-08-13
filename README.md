# Cardiac Patient Monitoring System

An individual, curriculum-aligned Machine Learning project analyzing the UCI Cleveland Heart
Disease dataset: data cleaning, exploratory data analysis, supervised binary classification,
leakage-free pipelines, and unsupervised structure discovery (clustering + PCA).

**This is an educational ML analysis, not a clinical diagnostic system.** It does not provide
diagnosis, treatment recommendations, or emergency guidance, and no output should be used for
medical decision-making.

---

## 1. Project Overview

Built end-to-end in eight sequential Jupyter notebooks, this project covers the full ML
lifecycle: environment setup → data loading → cleaning → EDA/statistics → baseline model →
model comparison + cross-validation → feature engineering + pipeline → clustering/PCA →
findings & limitations.

## 2. Objective

Predict presence vs. absence of heart disease (binary classification) from 13 patient features,
using models and techniques covered in the training curriculum (Logistic Regression, Random
Forest, Scikit-learn Pipelines, K-Means, PCA), while explaining results in plain, defensible
language — no deep learning, no LLMs, no production deployment.

## 3. Dataset

- **Source:** [UCI Machine Learning Repository — Heart Disease (Cleveland)](https://archive.ics.uci.edu/dataset/45/heart+disease), DOI `10.24432/C52P4X`
- **Size:** 303 observations, 13 features, 1 target (`num`, binarized to `target`)
- **Missing values:** 6 total (`ca`: 4, `thal`: 2) — see `outputs/results/phase2_data_quality_report.md`
- **Class balance:** 164 absence (54.1%) / 139 presence (45.9%)
- Raw file preserved unchanged at `data/raw/heart_disease_cleveland_raw.csv`; all derived files
  live under `data/processed/`.

## 4. Data Dictionary

See `data/data_dictionary.md` for the full feature-by-feature description (type, meaning, role,
value codes, missing counts). Quick summary:

| Feature | Type | Role |
|---|---|---|
| age, trestbps, chol, thalach, oldpeak | Numerical | Feature |
| sex, cp, fbs, restecg, exang, slope, ca, thal | Categorical | Feature |
| num | Integer (5-class) | Original target (preserved, unused for modeling directly) |
| target | Binary (0/1) | Modeling target (derived from `num`) |

## 5. Environment Setup

Requires Python 3.10+.

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 6. Installation

```bash
git clone <this-repo-url>
cd cardiac-patient-monitoring
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

## 7. How to Run

Run the notebooks **in order** from `notebooks/` — each one depends on files saved by the
previous one (raw CSV → processed CSVs → saved metrics/pipeline):

| # | Notebook | Produces |
|---|---|---|
| 01 | `01_environment_and_data_loading.ipynb` | `data/processed/heart_disease_cleveland_stage1.csv` |
| 02 | `02_data_cleaning_and_quality.ipynb` | `data/processed/..._stage2.csv`, data-quality report |
| 03 | `03_eda_statistics_visualization.ipynb` | 7 figures in `outputs/figures/` |
| 04 | `04_baseline_model.ipynb` | Baseline metrics, confusion matrix, ROC curve |
| 05 | `05_model_comparison_evaluation.ipynb` | 2nd model, CV, comparison table |
| 06 | `06_feature_engineering_pipeline.ipynb` | `models/cardiac_pipeline.pkl` |
| 07 | `07_clustering_pca.ipynb` | Clustering + PCA figures and results |
| 08 | `08_findings_and_limitations.ipynb` | `outputs/results/phase8_findings_and_limitations.md` |

To reproduce everything from scratch (as verified during Phase 9):

```bash
cd notebooks
for nb in 01_environment_and_data_loading 02_data_cleaning_and_quality \
          03_eda_statistics_visualization 04_baseline_model \
          05_model_comparison_evaluation 06_feature_engineering_pipeline \
          07_clustering_pca 08_findings_and_limitations; do
  jupyter nbconvert --to notebook --execute --inplace "${nb}.ipynb"
done
```

## 8. Methodology

1. **Cleaning:** missing values quantified and imputation strategy documented (median for `ca`,
   mode for `thal`), applied only inside train-fit pipelines — never on the raw file.
2. **EDA:** descriptive statistics, distribution/outlier analysis (IQR), correlation heatmap,
   categorical/bivariate breakdowns — every chart followed by written interpretation.
3. **Supervised learning:** stratified 80/20 train/test split (`random_state=42`), Logistic
   Regression baseline, Random Forest comparison model, both evaluated identically.
4. **Evaluation:** stratified 5-fold cross-validation, confusion matrices, accuracy/precision/
   recall/F1/ROC-AUC, with recall prioritized given the medical framing (false negatives costlier
   than false positives).
5. **Feature engineering & pipeline:** two domain-justified engineered features
   (`hr_reserve_ratio`, `bp_category`) folded into a single `ColumnTransformer` + `Pipeline`,
   fit only on training data (leakage-free).
6. **Unsupervised learning:** K-Means (`k` chosen via elbow + silhouette) and PCA (2D), target
   excluded from the clustering input and used only post-hoc for interpretation.

## 9. Models

| Model | Role |
|---|---|
| Logistic Regression | Baseline — interpretable linear reference point |
| Random Forest (`n_estimators=300`, `max_depth=5`) | Comparison model — captures non-linear/mixed-type structure |

Final saved artifact: `models/cardiac_pipeline.pkl` (Random Forest, selected for consistently
higher recall — see Section 11).

## 10. Evaluation

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC | CV F1 (mean ± std) |
|---|---|---|---|---|---|---|
| Logistic Regression | 0.869 | 0.813 | 0.929 | 0.867 | **0.958** | **0.825 ± 0.015** |
| Random Forest | **0.902** | **0.844** | **0.964** | **0.900** | 0.955 | 0.792 ± 0.037 |

Random Forest wins every single-split test metric; Logistic Regression is more stable across CV
folds. After feature engineering (Phase 6), Random Forest's test F1 slightly dropped (0.900 →
0.881) and Logistic Regression barely moved — a genuine null result, reported as-is.

## 11. Findings

Full findings and model-selection reasoning: `outputs/results/phase8_findings_and_limitations.md`.

- Strongest predictors: `thalach`, `oldpeak` (numerical); `cp`, `thal`, `exang` (categorical) —
  confirmed independently by both EDA correlation and Random Forest feature importances.
- K-Means (`k=2`) clusters aligned with the known target post-hoc (77.1% vs 22.1% disease-presence
  proportions), despite the target never being used to form them.
- **Random Forest selected** as the final model primarily for its consistently higher recall,
  the priority metric for this project's medical framing, with its higher CV variance disclosed
  as an explicit caveat.

## 12. Limitations

- Small sample (303 rows; 61-row test set) — metrics carry real uncertainty.
- Single-source, single-era data (Cleveland only, collected ~1988) — limited generalizability.
- ~68% male demographic imbalance inherited from the source data.
- Feature engineering did not improve results in this run.
- Modest unsupervised cluster separation (silhouette ≈ 0.175).
- Educational project only — **not validated or intended for clinical use.**

## 13. Project Structure

```text
cardiac-patient-monitoring/
├── data/
│   ├── raw/heart_disease_cleveland_raw.csv       # never modified
│   ├── processed/                                 # derived, reproducible checkpoints
│   └── data_dictionary.md
├── notebooks/
│   ├── 01_environment_and_data_loading.ipynb
│   ├── 02_data_cleaning_and_quality.ipynb
│   ├── 03_eda_statistics_visualization.ipynb
│   ├── 04_baseline_model.ipynb
│   ├── 05_model_comparison_evaluation.ipynb
│   ├── 06_feature_engineering_pipeline.ipynb
│   ├── 07_clustering_pca.ipynb
│   └── 08_findings_and_limitations.ipynb
├── models/
│   └── cardiac_pipeline.pkl                       # final leakage-free pipeline artifact
├── outputs/
│   ├── figures/                                   # 13 saved EDA/model/PCA figures
│   ├── confusion_matrix/                          # baseline + comparison-model matrices
│   └── results/                                   # all metrics, reports, findings (JSON/CSV/MD)
├── requirements.txt
└── README.md
```

## 14. Reproducibility

Verified during Phase 9: all generated files (`data/processed/`, `models/`, `outputs/`) were
deleted and every notebook was re-run in order, from a clean state, using only the raw CSV as
input. All 8 notebooks executed with zero errors and reproduced **identical metrics** to the
original runs, due to `random_state=42` fixed everywhere randomness is used.
