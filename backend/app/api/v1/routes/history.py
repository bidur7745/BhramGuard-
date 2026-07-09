from __future__ import annotations

from fastapi import APIRouter


router = APIRouter(prefix="/scans", tags=["history"])


# Scan history endpoints will be implemented after auth and manual migrations are ready.
