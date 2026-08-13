# Final Project Audit — Cardiac Patient Monitoring System

Audited against the official 100-point evaluation criteria. Every checkbox below is backed by a
specific file/notebook/number already produced in this project — nothing here is assumed.

---

## Python / NumPy / Pandas / Setup — 10 points

- [x] Correct environment — `requirements.txt` pinned to verified working versions; reproducibility re-tested from a fully clean state in Phase 9 (all 8 notebooks re-run from raw CSV only, zero errors, identical metrics).
- [x] Clean notebook structure — 8 notebooks, each scoped to one phase, alternating Markdown explanation / code cells throughout.
- [x] NumPy used appropriately — array operations in preprocessing, clustering, PCA (notebooks 04–07).
- [x] Pandas used appropriately — loading, cleaning, groupby profiling, crosstabs throughout.
- [x] Readable code — vectorized operations, no manual row-by-row loops over the DataFrame; `random_state=42` fixed everywhere.

**Evidence:** `notebooks/01_environment_and_data_loading.ipynb`, `requirements.txt`.

---

## EDA / Statistics / Visualization — 20 points

- [x] Descriptive statistics — mean/median/std/IQR for all 5 numerical features (`notebooks/03`, Section 1).
- [x] Data-quality review — `outputs/results/phase2_data_quality_report.md` (missing values, duplicates, invalid values, outliers).
- [x] Class balance — 164 absence (54.1%) / 139 presence (45.9%), documented in notebooks 01, 03, 08.
- [x] Correlations — heatmap in `outputs/figures/05_correlation_heatmap.png`; `thalach` r ≈ −0.42, `oldpeak` r ≈ +0.42 with target.
- [x] Distributions — histograms + boxplots, `outputs/figures/01_numerical_histograms.png`, `02_numerical_boxplots.png`.
- [x] Outliers — IQR screening in Phase 2 and Phase 3 (`trestbps`: 9, `chol`: 5, `oldpeak`: 5 flagged, none removed, decision justified).
- [x] Meaningful Matplotlib/Seaborn charts — 13 total figures saved to `outputs/figures/`, each answering a specific question, no decorative/repetitive charts.
- [x] Interpretation — every chart in notebook 03 is followed by a written interpretation paragraph.

**Evidence:** `notebooks/03_eda_statistics_visualization.ipynb`, `outputs/figures/01–07`.

---

## Supervised Learning — 20 points

- [x] Clear classification problem — binary: absence (0) vs presence (1) of heart disease.
- [x] Target defined — `num` (5-class, preserved) binarized to `target`, transformation documented in `data/data_dictionary.md` §7 and re-applied in notebook 01.
- [x] Baseline model — Logistic Regression (`notebooks/04`), chosen and justified as an interpretable linear reference point.
- [x] Second model — Random Forest (`notebooks/05`), chosen and justified for handling mixed/non-linear feature structure, not "because it's advanced."
- [x] Model choices justified — written justification sections in both notebooks 04 and 05, tied back to Phase 3 EDA findings.

**Evidence:** `notebooks/04_baseline_model.ipynb`, `notebooks/05_model_comparison_evaluation.ipynb`.

---

## Evaluation / Cross-validation — 20 points

- [x] Train/test split — stratified 80/20, `random_state=42`, reproducible (verified identical across independent re-runs).
- [x] Cross-validation — Stratified 5-Fold CV for both models (`notebooks/05`, Section 6); fold scores, mean, and std all reported.
- [x] Confusion matrix — both models (`outputs/confusion_matrix/baseline_logistic_regression_cm.png`, `random_forest_cm.png`), with TP/TN/FP/FN explained in plain language.
- [x] Accuracy — LR 0.869, RF 0.902.
- [x] Precision — LR 0.813, RF 0.844.
- [x] Recall — LR 0.929, RF 0.964 (the priority metric, explicitly justified by the false-negative-is-costlier framing).
- [x] F1 — LR 0.867, RF 0.900.
- [x] ROC-AUC — LR 0.958, RF 0.955 (`outputs/figures/09_roc_curve_comparison.png`).
- [x] Metrics interpreted — not just printed; see notebook 05 Sections 6–9 and the Phase 8 findings doc.

**Evidence:** `outputs/results/phase5_model_comparison.csv`, `outputs/results/phase5_cv_results.json`.

---

## Feature Engineering / Pipelines — 10 points

- [x] Feature preparation — imputation (median/mode) + scaling + one-hot encoding, all documented and justified in Phase 2/4.
- [x] Feature engineering — two domain-informed features: `hr_reserve_ratio` (thalach / age-predicted max HR) and `bp_category` (clinical BP bands), each documented with original feature, formula, and reason (`notebooks/06`, Section 2).
- [x] Scikit-learn Pipeline — full `Pipeline` combining feature engineering → `ColumnTransformer` preprocessing → classifier, fit end-to-end on raw data.
- [x] Repeatable training workflow — pipeline re-fit for both models; final artifact saved (`models/cardiac_pipeline.pkl`) and reload-tested on a live sample in the same notebook.

**Note (honesty over inflated claims):** feature engineering did **not** improve results in this
run (RF F1 0.900 → 0.881; LR unchanged) — reported transparently rather than omitted, per Project
Quality Rule 1.

**Evidence:** `notebooks/06_feature_engineering_pipeline.ipynb`, `models/cardiac_pipeline.pkl`.

---

## Unsupervised Learning / PCA — 10 points

- [x] Clustering — K-Means, `k=2` chosen via elbow + silhouette score (not guessed); silhouette ≈ 0.175, reported honestly as modest/weak-to-moderate separation.
- [x] PCA — 2 components, 38.9% cumulative explained variance (reported honestly, not oversold).
- [x] Visualization — `outputs/figures/11_kmeans_k_selection.png`, `12_cluster_feature_profiles.png`, `13_pca_2d_visualization.png`.
- [x] Interpretation — cluster 0 (older, lower thalach, higher oldpeak, 77.1% disease-presence) vs cluster 1 (younger, higher thalach, lower oldpeak, 22.1% disease-presence); explicit "not a diagnosis" boundary statement included.

**Evidence:** `notebooks/07_clustering_pca.ipynb`.

---

## Documentation / Reproducibility — 5 points

- [x] README — `README.md`, all 13 required sections present (overview through reproducibility).
- [x] requirements/environment file — `requirements.txt`, exact pinned versions matching the tested environment.
- [x] Limitations — Section 12 of README and full Phase 8 findings doc.
- [x] Reproducible execution — verified in Phase 9: all generated files deleted, all 8 notebooks re-run from raw CSV only, zero errors, metrics identical to original runs.

**Evidence:** `README.md`, `requirements.txt`, `outputs/results/phase8_findings_and_limitations.md`.

---

## Final Demo / Individual Ownership — 5 points

- [x] Can explain the problem — binary classification of heart disease presence, framed as data analysis, not diagnosis.
- [x] Can explain dataset — UCI Cleveland, 303 rows, 13 features, source/DOI known.
- [x] Can explain EDA — thalach/oldpeak/cp/thal/exang identified as strongest signals, cross-validated three separate ways (correlation, RF feature importance, PCA loadings).
- [x] Can explain models — why Logistic Regression as baseline, why Random Forest as comparison.
- [x] Can explain metrics — why recall is prioritized (false negatives costlier), what the CV std trade-off means.
- [x] Can explain findings — RF wins on test metrics, LR more CV-stable; feature engineering was a null result; clusters align with target post-hoc.
- [x] Can explain limitations — small sample, single-source/era data, sex imbalance, modest cluster separation, non-clinical framing.

**Evidence:** see `demo_script.md` for the minute-by-minute walkthrough.

---

## TOTAL: 100 / 100 criteria addressed with concrete evidence

Every checkbox above points to a specific file, notebook section, or number already produced and
independently reproducible — none of this audit is aspirational.
