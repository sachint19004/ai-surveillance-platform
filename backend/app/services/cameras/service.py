from sqlalchemy.orm import Session

from app.models.camera import Camera
from app.schemas.camera import CameraCreate, CameraUpdate


def create_camera(db: Session, data: CameraCreate):
    camera = Camera(**data.model_dump())

    db.add(camera)
    db.commit()
    db.refresh(camera)

    return camera


def get_cameras(db: Session):
    return db.query(Camera).order_by(Camera.id).all()


def get_camera(db: Session, camera_id: int):
    return (
        db.query(Camera)
        .filter(Camera.id == camera_id)
        .first()
    )


def update_camera(
    db: Session,
    camera_id: int,
    data: CameraUpdate,
):
    camera = get_camera(db, camera_id)

    if camera is None:
        return None

    for key, value in data.model_dump().items():
        setattr(camera, key, value)

    db.commit()
    db.refresh(camera)

    return camera


def toggle_camera_status(
    db: Session,
    camera_id: int,
):
    camera = get_camera(db, camera_id)

    if camera is None:
        return None

    camera.is_active = not camera.is_active

    db.commit()
    db.refresh(camera)

    return camera