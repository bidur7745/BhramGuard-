from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class ScanRequest(BaseModel):
    text: str | None = Field(default=None, description="Message, email, or visible text to analyze.")
    url: str | None = Field(default=None, description="URL to analyze.")
    web: str | None = Field(default=None, description="Webpage text or HTML content to analyze.")


class ModelResult(BaseModel):
    kind: Literal["text", "url", "web"]
    label: int
    phishing_probability: float
    risk_score: float
    best_model_name: str | None = None


class ScanResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    risk_score: float
    risk_level: Literal["low", "medium", "high", "critical"]
    results: list[ModelResult]
