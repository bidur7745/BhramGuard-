from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.api.v1.deps import get_current_user, get_db_session
from backend.app.models.user import User
from backend.app.schemas.feedback import FeedbackCreate, FeedbackResponse
from backend.app.services.feedback_service import create_feedback
from backend.app.services.history_service import get_user_scan

router = APIRouter(prefix="/scans/{scan_id}/feedback", tags=["feedback"])


@router.post("", response_model=FeedbackResponse, status_code=status.HTTP_201_CREATED)
def submit_feedback(
    scan_id: str,
    payload: FeedbackCreate,
    db: Session = Depends(get_db_session),
    current_user: User = Depends(get_current_user),
) -> FeedbackResponse:
    scan = get_user_scan(db, current_user.id, scan_id)
    if scan is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Scan was not found.")

    feedback = create_feedback(
        db,
        scan_id=scan.id,
        user_id=current_user.id,
        feedback_type=payload.feedback_type,
        note=payload.note,
    )
    return FeedbackResponse.model_validate(feedback)
