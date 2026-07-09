from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.camera import (
    CameraCreate,
    CameraResponse,
    CameraUpdate,
)
from app.services.cameras.service import (
    create_camera,
    get_cameras,
    get_camera,
    update_camera,
    toggle_camera_status,
)

router = APIRouter()

#post
@router.post(
    "/",
    response_model=CameraResponse,
)
def add_camera(
    data: CameraCreate,
    db: Session = Depends(get_db),
):
    return create_camera(db, data)

#get all
@router.get(
    "/",
    response_model=list[CameraResponse],
)
def list_cameras(
    db: Session = Depends(get_db),
):
    return get_cameras(db)

#get one
@router.get(
    "/{camera_id}",
    response_model=CameraResponse,
)
def get_single_camera(
    camera_id: int,
    db: Session = Depends(get_db),
):
    camera = get_camera(
        db,
        camera_id,
    )

    if camera is None:
        raise HTTPException(
            status_code=404,
            detail="Camera not found",
        )

    return camera

#put
@router.put(
    "/{camera_id}",
    response_model=CameraResponse,
)
def edit_camera(
    camera_id: int,
    data: CameraUpdate,
    db: Session = Depends(get_db),
):
    camera = update_camera(
        db,
        camera_id,
        data,
    )

    if camera is None:
        raise HTTPException(
            status_code=404,
            detail="Camera not found",
        )

    return camera

#patch
@router.patch(
    "/{camera_id}/status",
    response_model=CameraResponse,
)
def update_status(
    camera_id: int,
    db: Session = Depends(get_db),
):
    camera = toggle_camera_status(
        db,
        camera_id,
    )

    if camera is None:
        raise HTTPException(
            status_code=404,
            detail="Camera not found",
        )

    return camera