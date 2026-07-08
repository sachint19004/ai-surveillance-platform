from fastapi import APIRouter, Depends, HTTPException

import cv2
import numpy as np

from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    HTTPException,
    UploadFile,
)
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.known_face import KnownFaceCreate, KnownFaceResponse
from app.services.known_faces.embedding_service import generate_embedding
from app.services.known_faces.image_service import validate_image
from app.services.storage.image_storage import save_image
from app.services.known_faces.service import (
    create_known_face,
    delete_known_face,
    get_known_face,
    get_known_faces,
    toggle_face_status,
)

router = APIRouter()


@router.get(
    "/",
    response_model=list[KnownFaceResponse],
)
def list_known_faces(
    db: Session = Depends(get_db),
):
    return get_known_faces(db)


@router.get(
    "/{face_id}",
    response_model=KnownFaceResponse,
)
def get_face(
    face_id: int,
    db: Session = Depends(get_db),
):
    face = get_known_face(
        db,
        face_id,
    )

    if face is None:
        raise HTTPException(
            status_code=404,
            detail="Known face not found",
        )

    return face


@router.delete("/{face_id}")
def remove_face(
    face_id: int,
    db: Session = Depends(get_db),
):
    face = delete_known_face(
        db,
        face_id,
    )

    if face is None:
        raise HTTPException(
            status_code=404,
            detail="Known face not found",
        )

    return {
        "message": "Known face deleted successfully"
    }

@router.post(
    "/",
    response_model=KnownFaceResponse,
)
def create_face(
    name: str = Form(...),
    employee_id: str = Form(...),
    department: str = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    try:
        validate_image(image)

        image_path = save_image(image)

        image_np = cv2.imread(image_path)

        embedding = generate_embedding(image_np)

        data = KnownFaceCreate(
            name=name,
            employee_id=employee_id,
            department=department,
        )

        return create_known_face(
            db=db,
            data=data,
            image_path=image_path,
            embedding=embedding,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )
    
@router.patch(
    "/{face_id}/status",
    response_model=KnownFaceResponse,
)
def update_face_status(
    face_id: int,
    db: Session = Depends(get_db),
):
    face = toggle_face_status(
        db=db,
        face_id=face_id,
    )

    if face is None:
        raise HTTPException(
            status_code=404,
            detail="Known face not found",
        )

    return face