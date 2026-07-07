from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.known_face import KnownFaceResponse
from app.services.known_faces.service import (
    delete_known_face,
    get_known_face,
    get_known_faces,
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