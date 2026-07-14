from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models.event import EventType


class EventCreate(BaseModel):

    camera_id: int

    known_face_id: int | None = None

    event_type: EventType

    confidence: float | None = None

    image_path: str | None = None


class EventResponse(BaseModel):

    id: int

    camera_id: int

    known_face_id: int | None

    event_type: EventType

    confidence: float | None

    image_path: str | None

    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )