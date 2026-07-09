from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.camera import Camera
from app.services.cameras.stream_manager import camera_manager
from app.services.recognition.recognizer import recognize_frame

router = APIRouter()


@router.post("/{camera_id}/recognize")
def recognize_live(
    camera_id: int,
    db: Session = Depends(get_db),
):
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

    try:
        frame = camera_manager.get_frame(camera.id)

        face, score = recognize_frame(
            db=db,
            frame=frame,
        )

        if face is None:
            return {
                "recognized": False,
                "match_score": score,
            }

        return {
            "recognized": True,
            "id": face.id,
            "name": face.name,
            "employee_id": face.employee_id,
            "department": face.department,
            "match_score": score,
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )