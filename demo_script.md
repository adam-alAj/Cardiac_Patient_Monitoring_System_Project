# Final Demo Script — 5–10 Minutes
## Cardiac Patient Monitoring System

---

### Minute 0–1 — Problem

> "This project builds a binary classifier for heart disease presence versus absence, using the
> UCI Cleveland Heart Disease dataset. It's framed as an educational data-analysis and machine-
> learning exercise, not a diagnostic tool — I never claim clinical validity. The target started
> as a 5-class variable (`num`, 0–4) which I binarized: 0 stays absence, 1–4 collapse to
> presence, per the dataset's own documentation."

*(Optional visual: `data/data_dictionary.md` §7)*

---

### Minute 1–2 — Dataset

> "303 patients, 13 features, from the UCI Machine Learning Repository, DOI 10.24432/C52P4X. Mix
> of numerical (age, blood pressure, cholesterol, max heart rate, ST depression) and categorical
> (chest pain type, thalium test result, etc.) features. Only 6 missing values total, in two
> columns — a very clean dataset. Class balance is close to even: 164 absence, 139 presence."

*(Show: `outputs/results/phase2_data_quality_report.md`)*

---

### Minute 2–3 — EDA

> "Two figures tell most of the story. The correlation heatmap shows max heart rate (`thalach`)
> negatively correlated with disease presence, and ST depression (`oldpeak`) positively
> correlated — both around ±0.42, and both make physiological sense: reduced exercise capacity and
> larger ST depression both signal cardiac stress. The categorical breakdown shows chest pain type
> 4 — asymptomatic — paradoxically associated with *higher* disease presence, which is a known
> quirk in this dataset: asymptomatic patients here were often referred for angiography due to
> other risk factors."

*(Show: `outputs/figures/05_correlation_heatmap.png`, `06_categorical_vs_target.png`)*

---

### Minute 3–5 — Supervised Learning

> "I trained Logistic Regression as my baseline — simple, interpretable, sets the bar. Then Random
> Forest as the comparison model, chosen because it handles the mixed numeric/categorical
> structure and the non-linear patterns I saw in EDA, like that chest-pain effect, without
> assuming linearity. Both were trained and evaluated on an identical stratified 80/20 split, so
> the comparison is fair."

*(Show: `notebooks/04_baseline_model.ipynb` Section 4, `notebooks/05` Section 2)*

---

### Minute 5–6 — Evaluation

> "Here's the real result — Random Forest wins on every test-set metric: 90.2% accuracy versus
> 86.9%, and critically, 96.4% recall versus 92.9%. Recall is the metric I care about most here,
> because a false negative — telling a sick patient they're fine — is far more dangerous than a
> false positive that just costs a follow-up test. But — and I want to be honest about this —
> Logistic Regression was *more stable* across 5-fold cross-validation: standard deviation of
> 0.015 versus 0.037 for Random Forest. So Random Forest looks better on this one split, but it's
> also more sensitive to which rows end up in that split."

*(Show: confusion matrices in `outputs/confusion_matrix/`, comparison table in
`outputs/results/phase5_model_comparison.csv`)*

---

### Minute 6–7 — Pipeline

> "Everything — imputation, scaling, one-hot encoding, and two engineered features — is wrapped in
> a single Scikit-learn Pipeline, fit only on training data, to prevent leakage. The engineered
> features were `hr_reserve_ratio`, which normalizes max heart rate by age-predicted maximum, and
> `bp_category`, clinical blood-pressure bands. Honest result: they didn't help. Random Forest's
> F1 actually dropped slightly, 0.900 to 0.881, and Logistic Regression barely moved. I'm reporting
> that as a real finding, not hiding it."

*(Show: `notebooks/06_feature_engineering_pipeline.ipynb` Section 7, `models/cardiac_pipeline.pkl`)*

---

### Minute 7–8 — Unsupervised Learning

> "Separately, I ran K-Means clustering and PCA — without using the target at all — to see if the
> data has natural structure. Elbow and silhouette scores both pointed to 2 clusters, though the
> silhouette score was modest, around 0.175, so I'm not claiming sharp separation. What's
> interesting: after clustering, one group turned out to be 77% disease-presence and the other 22%
> — the clusters weren't told about the target, but they landed close to it anyway. That's a nice
> independent cross-check of the supervised findings, not a diagnosis."

*(Show: `outputs/figures/13_pca_2d_visualization.png`)*

---

### Minute 8–9 — Findings

> "Three things carried through the whole project consistently: `thalach`, `oldpeak`, and `thal`
> showed up as top signals in EDA correlation, Random Forest feature importance, *and* PCA
> loadings — three independent methods agreeing is the strongest evidence I have. Random Forest is
> my selected model for its recall advantage, with the CV-stability trade-off disclosed."

---

### Minute 9–10 — Limitations

> "This is a small dataset — 303 rows, a 61-row test set — so metrics have real uncertainty; one
> misclassified patient moves the numbers by over a percentage point. It's single-source,
> single-era data from one hospital in the late 1980s, and about 68% male, so I can't claim this
> generalizes broadly. And to say it one more time: this is an educational exercise, not a
> clinical tool."

---

## Quick-reference number sheet (keep this open during Q&A)

| Metric | Logistic Regression | Random Forest |
|---|---|---|
| Accuracy | 0.869 | 0.902 |
| Precision | 0.813 | 0.844 |
| Recall | 0.929 | 0.964 |
| F1 | 0.867 | 0.900 |
| ROC-AUC | 0.958 | 0.955 |
| CV F1 mean ± std | 0.825 ± 0.015 | 0.792 ± 0.037 |

- Dataset: 303 rows, 13 features, 6 missing values (`ca`: 4, `thal`: 2)
- Class balance: 54.1% absence / 45.9% presence
- K-Means: k=2, silhouette ≈ 0.175, clusters 77.1% vs 22.1% disease-presence
- PCA: 2 components = 38.9% explained variance
