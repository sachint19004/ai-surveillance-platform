import numpy as np


def cosine_similarity(embedding1, embedding2):
    embedding1 = np.frombuffer(embedding1, dtype=np.float32)
    embedding2 = np.frombuffer(embedding2, dtype=np.float32)

    return np.dot(
        embedding1,
        embedding2,
    ) / (
        np.linalg.norm(embedding1)
        * np.linalg.norm(embedding2)
    )