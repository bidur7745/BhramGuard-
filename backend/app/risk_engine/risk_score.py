from __future__ import annotations

from typing import Any

from backend.app.risk_engine.predict import predict_text, predict_url, predict_web


def risk_level(score: float) -> str:
    if score >= 80:
        return "critical"
    if score >= 60:
        return "high"
    if score >= 35:
        return "medium"
    return "low"


def combine_risk_scores(results: list[dict[str, Any]]) -> dict[str, Any]:
    active_results = [result for result in results if result is not None]
    if not active_results:
        return {"risk_score": 0.0, "risk_level": "low", "results": []}

    score = sum(float(result["risk_score"]) for result in active_results) / len(active_results)
    return {
        "risk_score": round(score, 2),
        "risk_level": risk_level(score),
        "results": active_results,
    }


def analyze_content(text: str | None = None, url: str | None = None, web: str | None = None) -> dict[str, Any]:
    results: list[dict[str, Any]] = []
    if text:
        results.append(predict_text(text))
    if url:
        results.append(predict_url(url))
    if web:
        results.append(predict_web(web))
    return combine_risk_scores(results)
