from datetime import datetime
from enum import Enum

from sqlalchemy import (
    DateTime,
    Enum as SQLEnum,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class EventType(str, Enum):
    KNOWN_FACE = "KNOWN_FACE"
    UNKNOWN_FACE = "UNKNOWN_FACE"
    CAMERA_STARTED = "CAMERA_STARTED"
    CAMERA_STOPPED = "CAMERA_STOPPED"
    CAMERA_OFFLINE = "CAMERA_OFFLINE"


class Event(Base):

    __tablename__ = "events"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    camera_id: Mapped[int] = mapped_column(
        ForeignKey("cameras.id"),
        nullable=False,
    )

    known_face_id: Mapped[int | None] = mapped_column(
        ForeignKey("known_faces.id"),
        nullable=True,
    )

    event_type: Mapped[EventType] = mapped_column(
        SQLEnum(EventType),
        nullable=False,
    )

    confidence: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    image_path: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )