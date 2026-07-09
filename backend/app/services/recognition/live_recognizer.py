import numpy as np
from sqlalchemy.orm import Session

from app.models.known_face import KnownFace
from app.services.known_faces.embedding_service import detect_faces
from app.services.recognition.drawing import (
    draw_known,
    draw_unknown,
)
from app.services.recognition.matcher import find_best_match


def process_frame(
    db: Session,
    frame,
):
    detected_faces = detect_faces(frame)

    known_faces = (
        db.query(KnownFace)
        .filter(KnownFace.is_active == True)
        .all()
    )

    for detected_face in detected_faces:

        embedding = (
            detected_face.embedding
            .astype(np.float32)
            .tobytes()
        )

        match, score = find_best_match(
            embedding,
            known_faces,
        )

        if match:

            draw_known(
                frame,
                detected_face.bbox,
                match.name,
                score,
            )

        else:

            draw_unknown(
                frame,
                detected_face.bbox,
            )

    return frame