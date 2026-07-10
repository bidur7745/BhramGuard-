from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.api.v1.deps import get_current_user, get_db_session
from backend.app.models.user import User
from backend.app.schemas.scan import ScanHistoryResponse
from backend.app.services.history_service import get_user_scan, list_user_scans

router = APIRouter(prefix="/scans", tags=["history"])


@router.get("", response_model=list[ScanHistoryResponse])
def list_scans(
    db: Session = Depends(get_db_session),
    current_user: User = Depends(get_current_user),
) -> list[ScanHistoryResponse]:
    return [ScanHistoryResponse.model_validate(scan) for scan in list_user_scans(db, current_user.id)]


@router.get("/{scan_id}", response_model=ScanHistoryResponse)
def read_scan(
    scan_id: str,
    db: Session = Depends(get_db_session),
    current_user: User = Depends(get_current_user),
) -> ScanHistoryResponse:
    scan = get_user_scan(db, current_user.id, scan_id)
    if scan is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Scan was not found.")
    return ScanHistoryResponse.model_validate(scan)
