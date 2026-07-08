from sqlalchemy.orm import Session

from app.models.known_face import KnownFace
from app.schemas.known_face import KnownFaceCreate


def create_known_face(
    db: Session,
    data: KnownFaceCreate,
    image_path: str,
    embedding: bytes,
):
    face = KnownFace(
        name=data.name,
        employee_id=data.employee_id,
        department=data.department,
        image_path=image_path,
        embedding=embedding,
    )

    db.add(face)
    db.commit()
    db.refresh(face)

    return face


def get_known_faces(db: Session):
    return (
        db.query(KnownFace)
        .order_by(KnownFace.id)
        .all()
    )


def get_known_face(
    db: Session,
    face_id: int,
):
    return (
        db.query(KnownFace)
        .filter(KnownFace.id == face_id)
        .first()
    )


def delete_known_face(
    db: Session,
    face_id: int,
):
    face = get_known_face(db, face_id)

    if face is None:
        return None

    db.delete(face)
    db.commit()

    return face

def toggle_face_status(
    db: Session,
    face_id: int,
):
    face = get_known_face(
        db,
        face_id,
    )

    if face is None:
        return None

    face.is_active = not face.is_active

    db.commit()
    db.refresh(face)

    return face