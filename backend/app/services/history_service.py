from __future__ import annotations

from sqlalchemy.orm import Session

from backend.app.models.scan import Scan


def list_user_scans(db: Session, user_id: str) -> list[Scan]:
    return (
        db.query(Scan)
        .filter(Scan.user_id == user_id)
        .order_by(Scan.created_at.desc())
        .all()
    )


def get_user_scan(db: Session, user_id: str, scan_id: str) -> Scan | None:
    return db.query(Scan).filter(Scan.user_id == user_id, Scan.id == scan_id).first()
