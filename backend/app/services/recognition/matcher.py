from app.services.recognition.similarity import cosine_similarity


MATCH_THRESHOLD = 0.60


def find_best_match(
    embedding,
    known_faces,
):
    best_face = None
    best_score = 0.0

    for face in known_faces:

        score = cosine_similarity(
            embedding,
            face.embedding,
        )

        if score > best_score:
            best_score = score
            best_face = face

    if best_score >= MATCH_THRESHOLD:
        return best_face, float(best_score)

    return None, float(best_score)