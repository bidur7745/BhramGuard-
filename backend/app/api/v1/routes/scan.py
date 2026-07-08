from __future__ import annotations

from fastapi import APIRouter, HTTPException

from backend.app.risk_engine.risk_score import analyze_content
from backend.app.schemas.scan import ScanRequest, ScanResponse


router = APIRouter(prefix="/scan", tags=["scan"])


@router.post("", response_model=ScanResponse)
def scan_content(payload: ScanRequest) -> ScanResponse:
    if not payload.text and not payload.url and not payload.web:
        raise HTTPException(status_code=400, detail="Provide at least one of text, url, or web.")

    result = analyze_content(text=payload.text, url=payload.url, web=payload.web)
    return ScanResponse.model_validate(result)
