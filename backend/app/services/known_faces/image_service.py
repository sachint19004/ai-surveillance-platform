from PIL import Image


ALLOWED_TYPES = {
    ".jpg",
    ".jpeg",
    ".png",
}


def validate_image(file):
    extension = file.filename.lower()

    if not extension.endswith(tuple(ALLOWED_TYPES)):
        raise ValueError("Unsupported image format")

    try:
        Image.open(file.file)

        file.file.seek(0)

    except Exception:
        raise ValueError("Invalid image")