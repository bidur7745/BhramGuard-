from __future__ import annotations

from sqlalchemy.orm import Session

from backend.app.models.scan import Scan


def create_scan(
    db: Session,
    *,
    user_id: str,
    input_text: str | None,
    input_url: str | None,
    input_web: str | None,
    risk_score: float,
    risk_level: str,
    model_results: list[dict],
) -> Scan:
    scan = Scan(
        user_id=user_id,
        input_text=input_text,
        input_url=input_url,
        input_web=input_web,
        risk_score=risk_score,
        risk_level=risk_level,
        model_results={"results": model_results},
    )
    db.add(scan)
    db.commit()
    db.refresh(scan)
    return scan
