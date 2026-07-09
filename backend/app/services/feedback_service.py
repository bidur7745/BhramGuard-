from __future__ import annotations

from sqlalchemy.orm import Session

from backend.app.models.feedback import Feedback


def create_feedback(
    db: Session,
    *,
    scan_id: str,
    user_id: str,
    feedback_type: str,
    note: str | None,
) -> Feedback:
    feedback = Feedback(
        scan_id=scan_id,
        user_id=user_id,
        feedback_type=feedback_type,
        note=note,
    )
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    return feedback
