import cv2

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.database.session import SessionLocal
from app.models.camera import Camera
from app.services.cameras.stream_manager import camera_manager
from app.services.recognition.live_recognizer import process_frame

router = APIRouter()


@router.get("/{camera_id}")
def live_video(camera_id: int):

    db: Session = SessionLocal()

    camera = (
        db.query(Camera)
        .filter(Camera.id == camera_id)
        .first()
    )

    if camera is None:
        raise HTTPException(
            status_code=404,
            detail="Camera not found",
        )

    camera_manager.open_camera(
        camera.id,
        camera.source,
    )

    try:

        while True:

            frame = camera_manager.get_frame(camera.id)

            frame = process_frame(
                db=db,
                frame=frame,
            )

            cv2.imshow(
                "AI Surveillance Platform",
                frame,
            )

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:

        camera_manager.release_camera(camera.id)

        db.close()

        cv2.destroyAllWindows()

    return {
        "status": "Video stopped"
    }