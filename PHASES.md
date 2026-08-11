# Cardiac Patient Monitoring System — Project Phases

## 1. Project Overview

This project is an individual AI & Machine Learning project based on the skills covered in the training track:

- Python
- NumPy
- Pandas
- Matplotlib
- Jupyter Notebook
- Statistics and probability
- Linear algebra refreshers
- Exploratory Data Analysis (EDA)
- Supervised learning
- Model evaluation
- Feature engineering
- Scikit-learn Pipelines
- Clustering
- Dimensionality reduction / PCA

The project is notebook/script based. No web API, frontend, mobile application, or production deployment is required.

### Main objective

Build a curriculum-aligned machine-learning analysis using synthetic or public cardiac-related data.

The project must:

1. Clean and prepare the dataset.
2. Explore and understand the data statistically.
3. Perform EDA and meaningful visualizations.
4. Define a clear classification problem.
5. Train a simple baseline classification model.
6. Train at least one additional comparison classifier.
7. Evaluate the models correctly using train/test splitting, cross-validation, and appropriate metrics.
8. Analyze confusion matrices and explain false positives and false negatives.
9. Perform feature engineering.
10. Build a reusable Scikit-learn Pipeline.
11. Perform an unsupervised analysis using clustering and/or dimensionality reduction such as PCA.
12. Document the methodology, findings, limitations, and reproducibility instructions.
13. Prepare a 5–10 minute individual demonstration.

### Important project boundary

This is an educational machine-learning analysis, not a clinical system.

The project must NOT provide:

- Clinical diagnosis
- Treatment recommendations
- Emergency instructions
- Medical decision-making
- Identifiable patient data
- Deep learning
- Neural networks
- LLMs
- Cloud ML platforms
- MLOps
- FastAPI deployment
- Production serving infrastructure
- Advanced explainability techniques not covered in the training
- Dependencies on another student's project or external production system

---

# 2. Overall Project Workflow

The complete implementation follows this workflow:

Dataset
    ↓
Project Definition
    ↓
Environment Setup
    ↓
Data Loading
    ↓
Data Cleaning
    ↓
Data Quality Analysis
    ↓
EDA + Statistics
    ↓
Visualization
    ↓
Target / Feature Definition
    ↓
Train/Test Split
    ↓
Baseline Classification Model
    ↓
Second Classification Model
    ↓
Cross-Validation
    ↓
Confusion Matrix
    ↓
Accuracy / Precision / Recall / F1 / ROC-AUC
    ↓
Model Comparison
    ↓
Feature Engineering
    ↓
Scikit-learn Pipeline
    ↓
Clustering
    ↓
PCA / Dimensionality Reduction
    ↓
Interpretation
    ↓
Findings
    ↓
Limitations
    ↓
README + Requirements
    ↓
Final Audit
    ↓
5–10 Minute Demo
    ↓
Final Submission

---

# 3. Recommended Project Structure

```text
cardiac-patient-monitoring/
│
├── data/
│   ├── raw/
│   │   └── cardiac_dataset.csv
│   │
│   └── processed/
│       └── cleaned_dataset.csv
│
├── notebooks/
│   └── cardiac_patient_monitoring.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   └── evaluation.py
│
├── models/
│   └── cardiac_pipeline.pkl
│
├── outputs/
│   ├── figures/
│   ├── confusion_matrix/
│   └── results/
│
├── README.md
├── requirements.txt
└── .gitignore
```

### Notes

The official project guide marks `src/` and `models/` as optional reusable components. The recommended structure includes:

- `data/` for the dataset and data dictionary.
- `notebooks/` for EDA, modeling, evaluation, and unsupervised analysis.
- `src/` for optional reusable functions.
- `models/` for optional saved Scikit-learn pipeline/model artifacts.
- `outputs/` for plots, confusion matrices, and result summaries.
- `requirements.txt` or `environment.yml` for reproducibility.
- `README.md` for setup, execution instructions, objective, and limitations.

---


# PHASE 1 — Environment + Dataset

## Official milestone

### M1 — Days 1–2

Required output:

- Python/Jupyter setup
- Dataset selection
- Data dictionary
- Initial Pandas cleaning

Review gate:

- Notebook opens.
- Dataset loads successfully.
- Dataset can be inspected.

## 1.1 Create Python environment

Use:

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

Create a reproducible environment.

## 1.2 Create requirements.txt

Record the packages used by the project.

The final file must reflect the environment actually used.

## 1.3 Select the dataset

The dataset must be:

- Public, synthetic, or properly de-identified.
- Cardiac-related.
- Suitable for classification.
- Suitable for EDA and statistical analysis.
- Suitable for the required supervised-learning work.
- Suitable for clustering and/or dimensionality reduction.

Do not select a dataset merely because it is popular.

Evaluate candidate datasets based on:

- Target clarity
- Number of observations
- Number and quality of features
- Data types
- Missing values
- Data quality
- Class balance
- Suitability for classification
- Suitability for EDA
- Suitability for unsupervised analysis
- Documentation/source quality

## 1.4 Create a data dictionary

Document every relevant column.

Recommended format:

| Feature | Type | Description | Role |
|---|---|---|---|
| Feature A | Numerical | Description | Feature |
| Feature B | Categorical | Description | Feature |
| Target | Binary/Categorical | Description | Target |

Do not invent meanings for columns. Use the dataset's documentation/source.

## 1.5 Load the dataset

Initial inspection should include:

```python
df.head()
df.tail()
df.shape
df.columns
df.info()
df.describe()
```

## Quality Gate

Before moving to Phase 2:

- Dataset is selected.
- Source is documented.
- Data dictionary exists.
- Target is understood.
- Columns and data types have been inspected.
- Notebook loads the dataset successfully.

---

# PHASE 2 — Data Cleaning + Data Quality

## Objective

Prepare a clean and trustworthy dataset before modeling.

## 2.1 Missing values

Inspect:

```python
df.isnull().sum()
```

Determine:

- Which columns contain missing values?
- How many?
- What percentage?
- Why might they exist?
- How should they be handled?

Possible approaches depend on the dataset and must be justified.

## 2.2 Duplicates

Inspect:

```python
df.duplicated().sum()
```

If duplicates exist:

- Determine whether they are true duplicates.
- Decide whether to remove them.
- Document the decision.

## 2.3 Invalid values

Inspect values that conflict with the meaning of the feature.

Do not automatically remove unusual values.

Determine whether each unusual value is:

- Invalid.
- A legitimate rare observation.
- A data-entry issue.
- Something requiring transformation.

## 2.4 Data types

Classify columns into:

- Numerical
- Categorical
- Target

Correct inappropriate data types where necessary.

## 2.5 Categorical variables

Identify categorical features.

Plan appropriate encoding through Scikit-learn preprocessing.

## 2.6 Initial data-quality report

Document:

- Missing values
- Duplicates
- Invalid values
- Data types
- Categorical features
- Numerical features
- Potential outliers
- Target class balance

## Quality Gate

Do not proceed until:

- Missing values are understood.
- Duplicates are handled.
- Invalid values are investigated.
- Data types are appropriate.
- Categorical variables are identified.
- Cleaning decisions are documented.

---

# PHASE 3 — EDA + Statistics + Visualization

## Official milestone

### M2 — Days 3–4

Required output:

- Descriptive statistics
- Probability/statistics review in context
- EDA
- Matplotlib visualizations

Review gate:

- EDA findings are complete.
- Data-quality notes are complete.

## Objective

Understand the dataset before training models.

EDA must contain meaningful analysis, not only raw tables.

## 3.1 Descriptive statistics

Analyze:

- Mean
- Median
- Standard deviation
- Minimum
- Maximum
- Quartiles
- Relevant distributions

Use Pandas and NumPy.

## 3.2 Distribution analysis

For relevant numerical variables, inspect distributions using suitable visualizations such as:

- Histograms
- Box plots

Questions should include:

- How are values distributed?
- Are there extreme observations?
- Are distributions approximately symmetric or skewed?
- Are there differences between groups where appropriate?

## 3.3 Categorical analysis

For categorical variables:

- Count categories.
- Visualize category frequencies.
- Identify rare categories where relevant.

## 3.4 Target class balance

Analyze the target distribution.

Example:

```text
Class 0 → ?
Class 1 → ?
```

Calculate both counts and proportions.

Document whether class imbalance exists.

## 3.5 Correlation analysis

Analyze relationships between numerical features.

Use an appropriate correlation matrix/visualization.

Interpret carefully.

Correlation must not be presented as proof of causation.

## 3.6 Outlier analysis

Use appropriate statistical and visual methods to identify potential outliers.

Do not automatically delete them.

Every removal/transformation decision must have a reason.

## 3.7 Visualization principles

Every visualization should answer a question.

Avoid:

- Unnecessary charts.
- Repetitive charts.
- Charts with no interpretation.

Each important chart should be followed by a concise interpretation.

## 3.8 Statistical interpretation

Connect statistics to the dataset.

The analysis should explain what the numbers mean rather than simply printing them.

## Quality Gate

Before moving to supervised learning:

- Descriptive statistics complete.
- Target distribution understood.
- Feature distributions analyzed.
- Correlations examined.
- Outliers investigated.
- Important relationships visualized.
- EDA findings documented.

---

# PHASE 4 — Supervised Learning: Baseline

## Official milestone

### M3 — Days 5–6

Required output:

- Supervised-learning problem definition.
- Train/test split.
- Baseline classifier.

Review gate:

- Baseline model works.
- First metrics are reproducible.

## 4.1 Define X and y

Conceptually:

```python
X = features
y = target
```

## 4.2 Train/test split

Separate the data into:

```text
Training Data
Testing Data
```

The training data is used to learn.

The test data is reserved for final evaluation.

The split strategy must be documented.

## 4.3 Baseline model

Use a simple classification model such as:

```text
Logistic Regression
```

as the baseline, consistent with the project guide.

## 4.4 Train

Fit the baseline using the training data.

## 4.5 Predict

Generate predictions on the appropriate evaluation data.

## 4.6 Initial evaluation

Calculate appropriate baseline metrics.

Record the results for later comparison.

## 4.7 Explain the baseline

Document:

- Why this model was selected.
- What role it plays as a baseline.
- What its initial performance indicates.

## Quality Gate

- Target correctly separated.
- Train/test split reproducible.
- Baseline model trains successfully.
- Predictions work.
- Initial metrics are recorded.

---

# PHASE 5 — Model Comparison + Evaluation

## Official milestone

### M4 — Days 7–8

Required output:

- Second classifier
- Cross-validation
- Confusion matrix
- Precision
- Recall
- F1-score
- Model comparison

Review gate:

- Model comparison is complete.
- Evaluation methodology is consistent and correct.

## 5.1 Select a second classifier

Choose a second Scikit-learn classifier covered by the training.

Selection should consider:

- Dataset characteristics.
- Feature types.
- Classification problem.
- Model assumptions.
- What was covered in training.

Do not choose a model simply because it is advanced.

## 5.2 Train second model

Train the second classifier using the same general evaluation methodology.

## 5.3 Use consistent evaluation

Both models must be evaluated consistently.

Avoid changing:

- Dataset split.
- Evaluation data.
- Metric methodology.

between models without justification.

## 5.4 Cross-validation

Use cross-validation to evaluate model stability.

For example, a K-fold approach can repeatedly use different folds for validation.

Record:

- Fold scores.
- Mean score.
- Variation/standard deviation where useful.

## 5.5 Confusion matrix

Create a confusion matrix.

Explain:

- True Positive
- True Negative
- False Positive
- False Negative

## 5.6 Accuracy

Explain the proportion of correct predictions.

## 5.7 Precision

Explain how reliable positive predictions are.

## 5.8 Recall

Explain how many actual positive instances are identified.

## 5.9 F1-score

Use F1 to summarize the balance between precision and recall.

## 5.10 ROC-AUC

Use ROC-AUC when appropriate for the classification setup.

## 5.11 Model comparison table

Create a table such as:

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC | CV Score |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | — | — | — | — | — | — |
| Model 2 | — | — | — | — | — | — |

Numbers will only be filled after executing the actual analysis.

## 5.12 Select the better model

Do not select a model based on accuracy alone.

Consider:

- Accuracy
- Precision
- Recall
- F1
- ROC-AUC where appropriate
- Cross-validation
- Confusion matrix

The final selection must be evidence-based.

## Quality Gate

- Two classifiers implemented.
- Same evaluation methodology used.
- Cross-validation completed.
- Confusion matrices produced.
- Required metrics calculated.
- Results compared.
- Model choice justified.

---

# PHASE 6 — Feature Engineering + Scikit-learn Pipeline

## Official milestone

### M5 — Days 9–10

Required output:

- Feature engineering.
- Scikit-learn Pipeline.
- Rerun training through the pipeline.

Review gate:

- Preprocessing and model training work as one repeatable pipeline.

## 6.1 Identify feature-processing needs

Depending on the dataset, identify:

- Missing-value handling.
- Numerical scaling.
- Categorical encoding.
- Feature transformations.
- Derived features where justified.

## 6.2 Feature engineering

Create meaningful features only when supported by the dataset.

Document:

- Original feature(s).
- New feature.
- Formula/logic.
- Reason for creating it.

Do not add arbitrary features simply to make the project look complex.

## 6.3 Preprocessing

Conceptually:

```text
Numerical Features
    ↓
Imputation if required
    ↓
Scaling if required

Categorical Features
    ↓
Imputation if required
    ↓
Encoding
```

## 6.4 Build Pipeline

Create a Scikit-learn Pipeline that combines preprocessing and model training.

Conceptually:

```text
Raw Data
   ↓
Preprocessing
   ↓
Feature Engineering
   ↓
Model
   ↓
Prediction
```

## 6.5 Data leakage prevention

Ensure that operations such as scaling, encoding, and imputation are learned from the training data rather than from the complete dataset before splitting.

The pipeline should help keep preprocessing and modeling consistent.

## 6.6 Re-run training

Train the selected workflow through the pipeline.

Confirm that:

- Training works.
- Prediction works.
- Evaluation works.
- The workflow is repeatable.

## Quality Gate

- Feature engineering documented.
- Preprocessing defined.
- Pipeline implemented.
- Model included in pipeline.
- Training runs through pipeline.
- Predictions work.
- No obvious data leakage.

---

# PHASE 7 — Unsupervised Learning: Clustering + PCA

## Official milestone

### M6 — Days 11–12

Required output:

- Clustering
- PCA/dimensionality reduction
- Visualization
- Interpretation

Review gate:

- Unsupervised analysis is complete and linked to the dataset.

## Objective

Explore the internal structure of the dataset without using the target as the learning signal.

---

## 7.1 Prepare data for unsupervised analysis

Use appropriate preprocessing.

Consider:

- Numerical scaling.
- Categorical handling where applicable.
- Feature selection.
- Removal of the target from the unsupervised learning input when appropriate.

The unsupervised analysis must be designed carefully so that the target does not improperly drive the discovered groups.

## 7.2 Clustering

Use a clustering method covered in the training, such as K-Means if it is part of the covered curriculum.

The method must be appropriate for the data.

## 7.3 Determine/justify cluster setup

If the selected clustering method requires choosing the number of clusters, use a suitable covered approach to support the choice.

Do not simply choose a number without explanation.

## 7.4 Analyze clusters

For each cluster, investigate feature patterns.

Questions:

- How large is each cluster?
- Which features differ?
- Are some groups clearly separated?
- Are groups overlapping?
- What patterns characterize each group?

## 7.5 PCA

Apply PCA or another dimensionality-reduction method covered in the training.

Conceptually:

```text
Many Features
     ↓
    PCA
     ↓
Principal Components
     ↓
2D Visualization
```

## 7.6 PCA visualization

Create a meaningful visualization of the reduced-dimensional representation.

Explain:

- What PC1 represents in broad terms.
- What PC2 represents.
- Whether observations appear separated or overlapping.
- Whether clustering structure is visible.

## 7.7 Interpretation boundary

Do not convert clusters into clinical diagnoses.

The purpose is to identify data patterns and structure.

## Quality Gate

- Unsupervised method implemented.
- Data appropriately prepared.
- Clustering and/or PCA completed.
- Visualization created.
- Results interpreted carefully.
- No unsupported clinical claims.

---

# PHASE 8 — Findings + Limitations

## Objective

Turn technical outputs into understandable conclusions.

## 8.1 Key findings

Create a concise section covering:

### Dataset findings

- Dataset size.
- Feature composition.
- Target distribution.
- Important data-quality findings.

### EDA findings

- Important distributions.
- Meaningful relationships.
- Correlation observations.
- Relevant outlier observations.

### Supervised-learning findings

- Baseline performance.
- Comparison-model performance.
- Cross-validation behavior.
- Confusion-matrix observations.
- Important metric differences.

### Unsupervised findings

- Cluster structure.
- PCA structure.
- Important patterns.

## 8.2 Model conclusion

State which model performed better according to the selected evidence.

Do not exaggerate the result.

## 8.3 Limitations

Document limitations such as:

- Dataset limitations.
- Sample-size limitations.
- Feature limitations.
- Data-quality limitations.
- Model limitations.
- Evaluation limitations.
- Generalization limitations.
- Non-clinical nature of the project.

## Quality Gate

The findings must answer:

1. What did we discover?
2. Which model performed better?
3. Why?
4. What did the unsupervised analysis reveal?
5. What are the project's limitations?

---

# PHASE 9 — Documentation + Reproducibility

## Official milestone

### M7 — Days 13–14

Required output:

- Notebook cleanup
- README
- Requirements/environment file
- Final results summary
- Demo preparation

Review gate:

- Complete submission runs from a clean environment.

## 9.1 Notebook documentation

Each major section should contain Markdown explaining:

- Purpose.
- Method.
- Result.
- Interpretation.

## 9.2 README

README should include:

```text
1. Project Overview
2. Objective
3. Dataset
4. Data Dictionary / Feature Description
5. Environment Setup
6. Installation
7. How to Run
8. Methodology
9. Models
10. Evaluation
11. Findings
12. Limitations
13. Project Structure
```

## 9.3 Requirements

Document exact project dependencies.

## 9.4 Reproducibility

A clean environment should be able to:

1. Install dependencies.
2. Open the notebook.
3. Load the dataset.
4. Execute the notebook.
5. Reproduce the analysis.
6. Reproduce the important results.

## 9.5 Final notebook execution

Restart the kernel and run the notebook from top to bottom.

Check every cell.

There must be no:

- Hidden variables.
- Manual steps.
- Missing imports.
- Broken file paths.
- Undefined variables.
- Random undocumented outputs.

---

# PHASE 10 — Final Audit + Demo

## 10.1 Final project audit

Review the complete project against the official 100-point evaluation criteria.

### Python / NumPy / Pandas / Setup — 10 points

```text
[ ] Correct environment
[ ] Clean notebook structure
[ ] NumPy used appropriately
[ ] Pandas used appropriately
[ ] Readable code
```

### EDA / Statistics / Visualization — 20 points

```text
[ ] Descriptive statistics
[ ] Data-quality review
[ ] Class balance
[ ] Correlations
[ ] Distributions
[ ] Outliers
[ ] Meaningful Matplotlib charts
[ ] Interpretation
```

### Supervised Learning — 20 points

```text
[ ] Clear classification problem
[ ] Target defined
[ ] Baseline model
[ ] Second model
[ ] Model choices justified
```

### Evaluation / Cross-validation — 20 points

```text
[ ] Train/test split
[ ] Cross-validation
[ ] Confusion matrix
[ ] Accuracy
[ ] Precision
[ ] Recall
[ ] F1
[ ] ROC-AUC where appropriate
[ ] Metrics interpreted
```

### Feature Engineering / Pipelines — 10 points

```text
[ ] Feature preparation
[ ] Feature engineering
[ ] Scikit-learn Pipeline
[ ] Repeatable training workflow
```

### Unsupervised Learning / PCA — 10 points

```text
[ ] Clustering and/or PCA
[ ] Visualization
[ ] Interpretation
```

### Documentation / Reproducibility — 5 points

```text
[ ] README
[ ] requirements/environment file
[ ] Limitations
[ ] Reproducible execution
```

### Final Demo / Individual Ownership — 5 points

```text
[ ] Can explain the problem
[ ] Can explain dataset
[ ] Can explain EDA
[ ] Can explain models
[ ] Can explain metrics
[ ] Can explain findings
[ ] Can explain limitations
```

---

# 10.2 Final Demo Plan — 5–10 Minutes

Recommended structure:

## Minute 0–1 — Problem

Explain:

- What is the project?
- What is the ML problem?
- What is the target?

## Minute 1–2 — Dataset

Explain:

- Source.
- Number of observations.
- Features.
- Target.
- Data-quality issues.

## Minute 2–3 — EDA

Show:

- One or two important visualizations.
- Class distribution.
- Important relationship/correlation.

Explain what was learned.

## Minute 3–5 — Supervised Learning

Explain:

- Baseline model.
- Second model.
- Why they were selected.
- Main metrics.

## Minute 5–6 — Evaluation

Show:

- Confusion matrix.
- Precision.
- Recall.
- F1.
- Cross-validation.

Explain false positives and false negatives.

## Minute 6–7 — Pipeline

Explain:

```text
Preprocessing
     ↓
Feature Engineering
     ↓
Model
```

## Minute 7–8 — Unsupervised Learning

Show:

- Clustering and/or PCA visualization.

Explain the observed structure.

## Minute 8–9 — Findings

State the most important results.

## Minute 9–10 — Limitations

Explain:

- Dataset limitations.
- Model limitations.
- Non-clinical nature of the project.

---

# 11. 14-Day Execution Schedule

| Day | Main Work | Required Evidence |
|---|---|---|
| Day 1 | Environment + Dataset research/selection | Environment + candidate comparison |
| Day 2 | Dataset loading + data dictionary + initial cleaning | **M1** |
| Day 3 | Descriptive statistics + initial EDA | Statistics |
| Day 4 | Visualizations + correlations + quality analysis | **M2** |
| Day 5 | Classification definition + split + baseline | Baseline |
| Day 6 | Baseline evaluation + reproducibility | **M3** |
| Day 7 | Second classifier | Comparison model |
| Day 8 | CV + confusion matrix + metrics | **M4** |
| Day 9 | Feature engineering + preprocessing | Feature workflow |
| Day 10 | Pipeline + repeatable training | **M5** |
| Day 11 | Clustering | Clustering analysis |
| Day 12 | PCA + visualization + interpretation | **M6** |
| Day 13 | Findings + limitations + README + requirements | Documentation |
| Day 14 | Final audit + clean execution + demo | **M7 + Submission** |

---

# 12. Project Quality Rules

Throughout implementation, follow these rules.

## Rule 1 — No invented results

Never manually create or assume:

- Accuracy
- Precision
- Recall
- F1
- ROC-AUC
- Cluster results

All results must come from executed code.

## Rule 2 — No unexplained code

Every important block should have a clear purpose.

## Rule 3 — Every chart must answer a question

Avoid decorative visualization.

## Rule 4 — No data leakage

Preprocessing must be performed correctly within the training workflow.

## Rule 5 — Fair model comparison

Models should use a consistent evaluation methodology.

## Rule 6 — Explain metrics

Do not simply print numbers.

## Rule 7 — No unsupported medical claims

The project is not a clinical diagnostic system.

## Rule 8 — Reproducibility

The notebook must execute from beginning to end in a clean environment.

## Rule 9 — Use only permitted data

Use public, synthetic, or properly de-identified data.

## Rule 10 — Individual ownership

The student must understand and be able to explain every important part of the project.

---

# 13. Final Deliverables

At submission time, the project should contain:

```text
[ ] Jupyter Notebook
[ ] Dataset
[ ] Data Dictionary
[ ] Data Cleaning
[ ] EDA
[ ] Statistics
[ ] Matplotlib Visualizations
[ ] Classification Problem
[ ] Train/Test Split
[ ] Baseline Classifier
[ ] Second Classifier
[ ] Cross-Validation
[ ] Confusion Matrix
[ ] Accuracy
[ ] Precision
[ ] Recall
[ ] F1-score
[ ] ROC-AUC where appropriate
[ ] Model Comparison
[ ] Feature Engineering
[ ] Scikit-learn Pipeline
[ ] Clustering and/or PCA
[ ] Unsupervised Visualization
[ ] Findings
[ ] Limitations
[ ] README.md
[ ] requirements.txt / environment.yml
[ ] Clean reproducible execution
[ ] 5–10 minute demo preparation
```

These deliverables correspond to the required submission items in the project guide. 

---

# 14. Final Success Definition

The project is considered ready only when all of the following are true:

```text
DATA
  ✓ Public/synthetic/de-identified
  ✓ Documented
  ✓ Cleaned
  ✓ Understood

EDA
  ✓ Statistics
  ✓ Distributions
  ✓ Correlations
  ✓ Class balance
  ✓ Visualizations
  ✓ Findings

SUPERVISED ML
  ✓ Target defined
  ✓ Train/test split
  ✓ Baseline
  ✓ Second classifier
  ✓ Cross-validation
  ✓ Metrics
  ✓ Confusion matrix
  ✓ Model comparison

PIPELINE
  ✓ Feature engineering
  ✓ Preprocessing
  ✓ Scikit-learn Pipeline
  ✓ Repeatable workflow
  ✓ No obvious data leakage

UNSUPERVISED ML
  ✓ Clustering and/or PCA
  ✓ Visualization
  ✓ Interpretation

DOCUMENTATION
  ✓ README
  ✓ requirements
  ✓ Limitations
  ✓ Reproducibility

FINAL
  ✓ Notebook runs top-to-bottom
  ✓ Clean environment tested
  ✓ Results are reproducible
  ✓ Demo prepared
  ✓ Student can explain the project independently
```

---

# 15. Official Project Milestones

The project guide defines the project as an **individual 14-day project**, with a reviewable milestone at the end of every two-day block. fileciteturn0file0L77-L80

```text
M1 — Days 1–2
Environment + Dataset + Data Dictionary + Cleaning

M2 — Days 3–4
Statistics + EDA + Visualization

M3 — Days 5–6
Classification + Train/Test + Baseline

M4 — Days 7–8
Second Model + CV + Confusion Matrix + Metrics

M5 — Days 9–10
Feature Engineering + Pipeline

M6 — Days 11–12
Clustering + PCA / Dimensionality Reduction

M7 — Days 13–14
Cleanup + README + Requirements + Results + Demo
```

The official guide also states that the final submission must be independently reviewable and that all two-day milestone outputs should be retained as evidence of progress. fileciteturn0file0L201-L209

