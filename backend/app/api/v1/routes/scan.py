from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.api.v1.deps import get_db_session, get_optional_current_user
from backend.app.models.user import User
from backend.app.risk_engine.risk_score import analyze_content
from backend.app.schemas.scan import ScanRequest, ScanResponse
from backend.app.services.scan_service import create_scan


router = APIRouter(prefix="/scan", tags=["scan"])


@router.post("", response_model=ScanResponse)
def scan_content(
    payload: ScanRequest,
    db: Session = Depends(get_db_session),
    current_user: User | None = Depends(get_optional_current_user),
) -> ScanResponse:
    if not payload.text and not payload.url and not payload.web:
        raise HTTPException(status_code=400, detail="Provide at least one of text, url, or web.")

    result = analyze_content(text=payload.text, url=payload.url, web=payload.web)
    if current_user is not None:
        scan = create_scan(
            db,
            user_id=current_user.id,
            input_text=payload.text,
            input_url=payload.url,
            input_web=payload.web,
            risk_score=result["risk_score"],
            risk_level=result["risk_level"],
            model_results=result["results"],
        )
        result["scan_id"] = scan.id

    return ScanResponse.model_validate(result)
