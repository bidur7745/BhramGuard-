from __future__ import annotations

import math
from functools import lru_cache
from pathlib import Path
from typing import Callable, Literal

import joblib
import pandas as pd
from scipy.sparse import csr_matrix, hstack

from backend.app.risk_engine.features.text_features import extract_text_features
from backend.app.risk_engine.features.url_features import extract_url_features
from backend.app.risk_engine.features.web_features import extract_web_features


ModelKind = Literal["text", "url", "web"]

MODEL_DIR = Path(__file__).resolve().parents[2] / "ml" / "models"
MODEL_FILES: dict[ModelKind, str] = {
    "text": "text_phishing_model.pkl",
    "url": "url_phishing_model.pkl",
    "web": "web_phishing_model.pkl",
}
FEATURE_EXTRACTORS: dict[ModelKind, Callable[[object], dict[str, float]]] = {
    "text": extract_text_features,
    "url": extract_url_features,
    "web": extract_web_features,
}


@lru_cache(maxsize=len(MODEL_FILES))
def load_artifact(kind: ModelKind) -> dict:
    model_path = MODEL_DIR / MODEL_FILES[kind]
    if not model_path.exists():
        raise FileNotFoundError(f"Missing {kind} model artifact: {model_path}")
    artifact = joblib.load(model_path)
    if not isinstance(artifact, dict):
        raise TypeError(f"{model_path} must contain a dict artifact")
    return artifact


def _manual_feature_frame(kind: ModelKind, value: str, artifact: dict) -> pd.DataFrame:
    feature_columns = artifact["manual_feature_columns"]
    features = FEATURE_EXTRACTORS[kind](value)
    frame = pd.DataFrame([features]).reindex(columns=feature_columns, fill_value=0)
    return frame.fillna(0)


def _score_model(model, matrix) -> float:
    if hasattr(model, "predict_proba"):
        return float(model.predict_proba(matrix)[0, 1])
    if hasattr(model, "decision_function"):
        margin = float(model.decision_function(matrix)[0])
        return 1.0 / (1.0 + math.exp(-margin))
    return float(model.predict(matrix)[0])


def predict(kind: ModelKind, value: str) -> dict[str, object]:
    artifact = load_artifact(kind)
    vectorizer = artifact["vectorizer"]
    model = artifact["model"]

    text_matrix = vectorizer.transform([value or ""])
    manual_frame = _manual_feature_frame(kind, value or "", artifact)

    scaler = artifact.get("manual_scaler")
    manual_values = scaler.transform(manual_frame) if scaler is not None else manual_frame.values
    matrix = hstack([text_matrix, csr_matrix(manual_values)])

    phishing_probability = _score_model(model, matrix)
    label = int(phishing_probability >= 0.5)

    return {
        "kind": kind,
        "label": label,
        "phishing_probability": phishing_probability,
        "risk_score": round(phishing_probability * 100, 2),
        "best_model_name": artifact.get("best_model_name"),
    }


def predict_text(text: str) -> dict[str, object]:
    return predict("text", text)


def predict_url(url: str) -> dict[str, object]:
    return predict("url", url)


def predict_web(content: str) -> dict[str, object]:
    return predict("web", content)
