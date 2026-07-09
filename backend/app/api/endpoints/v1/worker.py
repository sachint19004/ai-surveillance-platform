from fastapi import APIRouter

from app.database.session import get_db_session
from app.services.recognition.worker import (
    recognition_worker,
)

router = APIRouter()

#start worker
@router.post("/{camera_id}/start")
def start_worker(
    camera_id: int,
):

    recognition_worker.start(
        camera_id,
        get_db_session,
    )

    return {
        "status": "Recognition worker started"
    }

#stop worker 
@router.post("/{camera_id}/stop")
def stop_worker(
    camera_id: int,
):

    recognition_worker.stop(camera_id)

    return {
        "status": "Recognition worker stopped"
    }