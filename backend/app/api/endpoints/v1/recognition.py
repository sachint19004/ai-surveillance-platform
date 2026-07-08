from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.storage.image_storage import save_image
from app.services.known_faces.image_service import validate_image
from app.services.recognition.recognizer import recognize_face

router = APIRouter()


@router.post("/recognize")
def recognize(
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    try:
        validate_image(image)

        image_path = save_image(image)

        face, score = recognize_face(
            db=db,
            image_path=image_path,
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

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )