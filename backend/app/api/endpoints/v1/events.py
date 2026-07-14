from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.event import EventType
from app.schemas.event import EventCreate, EventResponse
from app.services.events.service import (
    create_event,
    get_event,
    get_events,
    get_camera_events,
    get_events_by_type,
)

router = APIRouter()

#post
@router.post(
    "/",
    response_model=EventResponse,
)
def add_event(
    data: EventCreate,
    db: Session = Depends(get_db),
):
    return create_event(db, data)

#get all events

@router.get(
    "/",
    response_model=list[EventResponse],
)
def list_events(
    db: Session = Depends(get_db),
):
    return get_events(db)

#get one event by id
@router.get(
    "/{event_id}",
    response_model=EventResponse,
)
def get_single_event(
    event_id: int,
    db: Session = Depends(get_db),
):
    event = get_event(
        db,
        event_id,
    )

    if event is None:
        raise HTTPException(
            status_code=404,
            detail="Event not found",
        )

    return event

#get events by camera id
@router.get(
    "/camera/{camera_id}",
    response_model=list[EventResponse],
)
def list_camera_events(
    camera_id: int,
    db: Session = Depends(get_db),
):
    return get_camera_events(
        db,
        camera_id,
    )

#get events by event type
@router.get(
    "/type/{event_type}",
    response_model=list[EventResponse],
)
def list_events_by_type(
    event_type: EventType,
    db: Session = Depends(get_db),
):
    return get_events_by_type(
        db,
        event_type,
    )

