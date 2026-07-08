from pathlib import Path
from uuid import uuid4

UPLOAD_DIR = Path("app/assets/known_faces")

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


def save_image(file):
    extension = Path(file.filename).suffix

    filename = f"{uuid4()}{extension}"

    destination = UPLOAD_DIR / filename

    with open(destination, "wb") as buffer:
        buffer.write(file.file.read())

    return str(destination)