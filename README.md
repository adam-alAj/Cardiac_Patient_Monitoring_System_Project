# Cardiac Patient Monitoring System

An individual **AI & Machine Learning project** built as part of the BinX Tech AI & ML Internship Program. This project applies the full training-track skillset — Python, NumPy, Pandas, Matplotlib, statistics & probability, EDA, supervised learning, model evaluation, feature engineering, Scikit-learn Pipelines, clustering, and PCA — to a public cardiac dataset, with a notebook-first, fully reproducible workflow.

> ⚠️ **Important boundary:** This is an **educational machine-learning analysis, not a clinical system**. It does NOT provide clinical diagnosis, treatment recommendations, emergency instructions, or medical decision-making, and it must never be used as such.

---

## 🎯 Objective

Build a curriculum-aligned, end-to-end machine-learning analysis that:

1. Cleans and prepares the dataset.
2. Explores and understands the data statistically.
3. Performs EDA with meaningful visualizations.
4. Defines a clear classification problem (presence vs. absence of heart disease).
5. Trains a simple baseline classifier (Logistic Regression).
6. Trains at least one additional comparison classifier.
7. Evaluates models correctly using train/test splitting, cross-validation, and appropriate metrics (Accuracy, Precision, Recall, F1, ROC-AUC).
8. Analyzes confusion matrices and explains false positives / false negatives.
9. Performs feature engineering.
10. Builds a reusable, leakage-free Scikit-learn Pipeline.
11. Performs an unsupervised analysis (clustering and/or PCA).
12. Documents methodology, findings, limitations, and reproducibility instructions.
13. Prepares a 5–10 minute individual demonstration.

---

## 📊 Dataset

**Heart Disease — Cleveland Database** (UCI Machine Learning Repository).

| Property | Value |
|---|---|
| UCI Dataset ID | 45 |
| Official Source | https://archive.ics.uci.edu/dataset/45/heart+disease |
| DOI | 10.24432/C52P4X |
| Task | Classification |
| Observations | 303 |
| Features | 13 |
| Raw Target | `num` (5 classes: 0–4) |
| Binary Target | `target` (0 = absence, 1 = presence), derived |
| Missing Values | Yes (`ca`: 4, `thal`: 2 — 1.98% of rows) |
| Retrieval Method | `ucimlrepo` package (dataset ID 45), programmatic |

The dataset was retrieved programmatically from UCI and stored unchanged at `data/raw/heart_disease_cleveland_raw.csv`. Per UCI documentation, patient names and social security numbers were already removed from the source database, so no patient identifiers are used.

### Target transformation (documented, non-destructive)

The original 5-class `num` target is transformed into a binary `target` column **only on derived datasets**:

```
num: 0 → target: 0  (absence of heart disease)
num: 1,2,3,4 → target: 1  (presence of heart disease)
```

The raw `num` column is always preserved in the raw file; the binary column is added to processed datasets only.

**Class balance (binary):** absence 164 (54.1%) vs presence 139 (45.9%) — close to balanced. No resampling needed; stratified splitting and stratified K-Fold CV preserve class proportions.

---

## 📖 Data Dictionary / Feature Description

The full, source-documented data dictionary (features, types, units, value sets, missing counts, and observed statistics) lives at [`data/data_dictionary.md`](./data/data_dictionary.md).

**Feature summary:**

| Feature | Type | Role | Description |
|---|---|---|---|
| age | Integer | Feature | Age in years |
| sex | Categorical | Feature | 0 = female, 1 = male |
| cp | Categorical | Feature | Chest pain type (1–4) |
| trestbps | Integer | Feature | Resting blood pressure (mm Hg) |
| chol | Integer | Feature | Serum cholesterol (mg/dl) |
| fbs | Categorical | Feature | Fasting blood sugar > 120 mg/dl |
| restecg | Categorical | Feature | Resting ECG results (0–2) |
| thalach | Integer | Feature | Maximum heart rate achieved |
| exang | Categorical | Feature | Exercise-induced angina |
| oldpeak | Real | Feature | ST depression induced by exercise |
| slope | Categorical | Feature | Slope of peak exercise ST segment (1–3) |
| ca | Integer | Feature | Major vessels colored by fluoroscopy (0–3); 4 missing |
| thal | Categorical | Feature | Thallium test result (3, 6, 7); 2 missing |
| num | Integer | Target (raw) | Diagnosis status (0–4), preserved |
| target | Integer | Target (binary) | 0 = absence, 1 = presence (derived) |

---

## 🧹 Data Cleaning & Quality (completed)

Two notebooks and two written reports cover the cleaning phase:

- **[01 — Environment, Dataset Loading & Initial Cleaning](./notebooks/01_environment_and_data_loading.ipynb)** *(Milestone M1)* — environment check, raw dataset load, initial inspection (`head`/`tail`/`info`/`describe`), missing-value identification, duplicate check, data-type classification, binary target definition, and the stage-1 processed snapshot.
- **[02 — Data Cleaning & Data Quality](./notebooks/02_data_cleaning_and_quality.ipynb)** *(Phase 2)* — missing-value strategy, duplicate & invalid-value checks, dtype classification, categorical encoding plan, IQR outlier screening, class-balance confirmation, and the stage-2 checkpoint.

**Key cleaning decisions (documented, nothing destructive):**

| Area | Finding | Decision |
|---|---|---|
| Missing values | `ca` (4), `thal` (2) | Median imputation for `ca`, mode imputation for `thal` — applied **inside the Pipeline, fit on training data only** (Phase 6) |
| Duplicates | 0 | None to remove |
| Invalid values | None | All categorical values within documented sets |
| Outliers (IQR) | `trestbps`: 9, `chol`: 5, `oldpeak`: 5, `thalach`: 1, `age`: 0 | Kept — legitimate rare clinical observations; reviewed visually in EDA |
| Encoding plan | `cp`, `restecg`, `slope`, `thal` (nominal) | One-hot encode; `sex`, `fbs`, `exang` passthrough (already binary) |
| Raw data | — | Never modified; all transforms go to `data/processed/` |

**Reports:** [`outputs/results/phase1_dataset_validation.md`](./outputs/results/phase1_dataset_validation.md) · [`outputs/results/phase2_data_quality_report.md`](./outputs/results/phase2_data_quality_report.md)

---

## 🧪 Methodology (planned workflow)

The project follows the 10-phase plan in [`PHASES.md`](./PHASES.md) (M1–M7 milestones over 14 days):

```text
Dataset → Project Definition → Environment Setup → Data Loading → Data Cleaning →
Data Quality → EDA + Statistics → Visualization → Target/Feature Definition →
Train/Test Split → Baseline Classifier → Second Classifier → Cross-Validation →
Confusion Matrix → Accuracy/Precision/Recall/F1/ROC-AUC → Model Comparison →
Feature Engineering → Scikit-learn Pipeline → Clustering → PCA →
Interpretation → Findings → Limitations → README + Requirements → Final Audit → Demo
```

### Progress tracker

| Phase | Milestone | Status |
|---|---|---|
| 1 — Environment + Dataset | M1 (Days 1–2) | ✅ Complete |
| 2 — Data Cleaning + Data Quality | M1 (Days 1–2) | ✅ Complete |
| 3 — EDA + Statistics + Visualization | M2 (Days 3–4) | ⏳ Next |
| 4 — Supervised Learning: Baseline | M3 (Days 5–6) | ⏳ Planned |
| 5 — Model Comparison + Evaluation | M4 (Days 7–8) | ⏳ Planned |
| 6 — Feature Engineering + Pipeline | M5 (Days 9–10) | ⏳ Planned |
| 7 — Unsupervised: Clustering + PCA | M6 (Days 11–12) | ⏳ Planned |
| 8 — Findings + Limitations | — | ⏳ Planned |
| 9 — Documentation + Reproducibility | M7 (Days 13–14) | ⏳ Planned |
| 10 — Final Audit + Demo | Submission | ⏳ Planned |

---

## 🤖 Models & Evaluation (planned)

- **Baseline model:** `LogisticRegression` — simple, interpretable, consistent with the project guide. Feature scaling required.
- **Comparison model:** one additional Scikit-learn classifier (e.g. `RandomForestClassifier` / `KNeighborsClassifier` / `SVC`), selected based on dataset characteristics and curriculum coverage — justified, not chosen "because it is advanced".
- **Evaluation:** consistent methodology across both models — stratified train/test split, 5-Fold Stratified Cross-Validation (fold scores + mean ± std), confusion matrix (with FP/FN interpretation), Accuracy, Precision, Recall, F1, ROC-AUC, and a final model-comparison table with an evidence-based winner.
- **Feature engineering:** meaningful derived features only, each documented (original features → formula → rationale).
- **Pipeline:** Scikit-learn `ColumnTransformer` + `Pipeline` handling imputation, encoding, and scaling **fit on training data only** to prevent data leakage.
- **Unsupervised:** K-Means clustering (cluster count justified via a covered method) and/or PCA with 2D visualization, interpreted without clinical claims.

> No metric, cluster, or model result will be reported until produced by executed code (project Rule 1 — no invented results).

---

## 📁 Project Structure

```text
cardiac-patient-monitoring/
├── data/
│   ├── raw/
│   │   └── heart_disease_cleveland_raw.csv      # Never modified
│   ├── processed/
│   │   ├── heart_disease_cleveland_stage1.csv   # Phase 1 snapshot (+ binary target)
│   │   └── heart_disease_cleveland_stage2.csv   # Phase 2 checkpoint
│   └── data_dictionary.md
├── notebooks/
│   ├── 01_environment_and_data_loading.ipynb
│   └── 02_data_cleaning_and_quality.ipynb
├── outputs/
│   └── results/
│       ├── phase1_dataset_validation.md
│       └── phase2_data_quality_report.md
├── src/
│   └── __init__.py                              # Reusable functions (optional)
├── PHASES.md                                    # Full 10-phase project plan
├── README.md                                    # ← You are here
├── requirements.txt
└── .gitignore
```

*Note: `models/` will be added for saved pipeline artifacts if/when Phase 6 is reached; `outputs/figures/` will hold plots from Phase 3 onward.*

---

## 🚀 Environment Setup & Installation

The project was developed on **Python 3.14** with Jupyter Notebooks (compatible with modern Python 3.x versions).

```bash
# 1. Clone the parent repository (with submodules)
git clone --recurse-submodules https://github.com/adam-alAj/BinX-ML-Internship.git
cd BinX_ML_Internship/Cardiac_Patient_Monitoring_System_Project

# 2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # Linux / macOS

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch Jupyter and open the notebooks
python -m jupyter notebook
```

**Core dependencies** (pinned in `requirements.txt`): `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `scipy`, `jupyter`, and `ucimlrepo` (dataset retrieval).

**Reproducibility rules:**
- Notebooks must run top-to-bottom from a clean environment.
- `data/raw/` is never modified — all cleaning output goes to `data/processed/`.
- Imputation, scaling, and encoding are fit on training data only (inside the Pipeline) to prevent leakage.

---

## ⚠️ Limitations

- **Not a clinical system:** results are for educational purposes and must not inform medical decisions.
- **Dataset size:** 303 observations is a small sample — limited statistical power and generalization confidence.
- **Single source:** only the Cleveland database is used (not Hungary/Switzerland/VA Long Beach).
- **Historical data (1989):** collected decades ago; clinical protocols and population characteristics may differ today.
- **Missing values** (`ca`, `thal`) are handled by imputation, which is an approximation.
- **No patient identifiers** are used; de-identification was performed by the original dataset maintainers.

---

## 🔗 Related

- [`PHASES.md`](./PHASES.md) — complete 10-phase project plan, milestones, quality gates, and demo plan
- [`data/data_dictionary.md`](./data/data_dictionary.md) — full feature documentation
- [Root Repository README](../README.md) — internship overview and progress tracker
