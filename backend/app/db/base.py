from __future__ import annotations

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Import models so Alembic/manual migrations can discover metadata.
from backend.app.models.feedback import Feedback  # noqa: E402,F401
from backend.app.models.scan import Scan  # noqa: E402,F401
from backend.app.models.user import User  # noqa: E402,F401
