from sqlalchemy.orm import Session

from app.models.event import Event, EventType
from app.schemas.event import EventCreate
from app.schemas.event import EventCreate
from app.models.event import EventType

def create_event(
    db: Session,
    data: EventCreate,
):
    event = Event(**data.model_dump())

    db.add(event)
    db.commit()
    db.refresh(event)

    return event


def get_events(db: Session):
    return (
        db.query(Event)
        .order_by(Event.created_at.desc())
        .all()
    )


def get_event(
    db: Session,
    event_id: int,
):
    return (
        db.query(Event)
        .filter(Event.id == event_id)
        .first()
    )


def get_camera_events(
    db: Session,
    camera_id: int,
):
    return (
        db.query(Event)
        .filter(Event.camera_id == camera_id)
        .order_by(Event.created_at.desc())
        .all()
    )


def get_events_by_type(
    db: Session,
    event_type: EventType,
):
    return (
        db.query(Event)
        .filter(Event.event_type == event_type)
        .order_by(Event.created_at.desc())
        .all()
    )

def log_recognition_event(
    db: Session,
    camera_id: int,
    face=None,
    score: float | None = None,
):
    if face is None:

        event = EventCreate(
            camera_id=camera_id,
            known_face_id=None,
            event_type=EventType.UNKNOWN_FACE,
            confidence=score,
            image_path=None,
        )

    else:

        event = EventCreate(
            camera_id=camera_id,
            known_face_id=face.id,
            event_type=EventType.KNOWN_FACE,
            confidence=score,
            image_path=None,
        )

    return create_event(
        db,
        event,
    )