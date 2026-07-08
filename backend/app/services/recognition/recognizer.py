import cv2

from sqlalchemy.orm import Session

from app.models.known_face import KnownFace
from app.services.known_faces.embedding_service import (
    generate_embedding,
)
from app.services.recognition.matcher import (
    find_best_match,
)


def recognize_face(
    db: Session,
    image_path: str,
):
    image = cv2.imread(image_path)

    embedding = generate_embedding(image)

    known_faces = (
        db.query(KnownFace)
        .filter(KnownFace.is_active == True)
        .all()
    )

    return find_best_match(
        embedding,
        known_faces,
    )