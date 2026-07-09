from insightface.app import FaceAnalysis
import numpy as np

app = FaceAnalysis(
    name="buffalo_l",
    providers=["CPUExecutionProvider"],
)

app.prepare(
    ctx_id=0,
    det_size=(640, 640),
)


def generate_embedding(image):
    faces = app.get(image)

    if len(faces) == 0:
        raise ValueError("No face detected")

    if len(faces) > 1:
        raise ValueError("Multiple faces detected")

    embedding = faces[0].embedding.astype(np.float32)

    return embedding.tobytes()

def detect_faces(image):
    """
    Returns all detected faces from an image.
    """

    return app.get(image)