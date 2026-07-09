from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


FeedbackType = Literal["false_positive", "false_negative", "correct", "uncertain"]


class FeedbackCreate(BaseModel):
    feedback_type: FeedbackType
    note: str | None = Field(default=None, max_length=1000)


class FeedbackResponse(BaseModel):
    id: str
    scan_id: str
    user_id: str
    feedback_type: FeedbackType
    note: str | None
    created_at: datetime
