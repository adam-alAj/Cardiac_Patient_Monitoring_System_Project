"""
Cardiac Patient Monitoring System — Feature Engineering

Contains CardiacFeatureEngineer, the custom Scikit-learn-compatible transformer used inside
the project's final Pipeline (see notebooks/06_feature_engineering_pipeline.ipynb).

This class lives here (rather than being defined inline in a notebook) specifically so that
the saved pipeline artifact (models/cardiac_pipeline.pkl) can be unpickled and reused from
any script or fresh Python session, not only from within the notebook that trained it.
"""

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class CardiacFeatureEngineer(BaseEstimator, TransformerMixin):
    """Adds two domain-informed engineered features:

    - hr_reserve_ratio: thalach / (220 - age)
        Proportion of the age-predicted maximum heart rate actually achieved during exercise.
        Normalizes 'thalach' for age, removing the age confound from a raw heart-rate reading.

    - bp_category: standard clinical resting-blood-pressure bands derived from 'trestbps'
        (Normal < 120, Elevated 120-129, High1 130-139, High2 >= 140 mm Hg).

    Stateless (no fitting required) — each engineered value is computed purely from that row's
    own age/thalach/trestbps using fixed, dataset-independent formulas, so this transformer
    introduces no data leakage regardless of where it sits relative to a train/test split.
    """

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X['hr_reserve_ratio'] = X['thalach'] / (220 - X['age'])

        bins = [-np.inf, 120, 130, 140, np.inf]
        labels = ['Normal', 'Elevated', 'High1', 'High2']
        X['bp_category'] = pd.cut(X['trestbps'], bins=bins, labels=labels)
        X['bp_category'] = X['bp_category'].astype(str)
        return X
