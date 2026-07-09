from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.camera import Camera
from app.services.cameras.stream_manager import camera_manager

router = APIRouter()

#open camera
@router.post("/{camera_id}/start")
def start_camera(
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

    camera_manager.open_camera(
        camera.id,
        camera.source,
    )

    return {
        "status": "Camera started"
    }

#stop camera
@router.post("/{camera_id}/stop")
def stop_camera(
    camera_id: int,
):
    camera_manager.release_camera(camera_id)

    return {
        "status": "Camera stopped"
    }

#Health check for camera stream
@router.get("/{camera_id}/health")
def health(
    camera_id: int,
):
    try:
        camera_manager.get_frame(camera_id)

        return {
            "status": "healthy"
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )