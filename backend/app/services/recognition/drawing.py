import cv2


GREEN = (0, 255, 0)
RED = (0, 0, 255)


def draw_known(frame, bbox, name, score):

    x1, y1, x2, y2 = map(int, bbox)

    cv2.rectangle(
        frame,
        (x1, y1),
        (x2, y2),
        GREEN,
        2,
    )

    cv2.putText(
        frame,
        f"{name} | {score*100:.1f}%",
        (x1, y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        GREEN,
        2,
    )


def draw_unknown(frame, bbox):

    x1, y1, x2, y2 = map(int, bbox)

    cv2.rectangle(
        frame,
        (x1, y1),
        (x2, y2),
        RED,
        2,
    )

    cv2.putText(
        frame,
        "INTRUDER",
        (x1, y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        RED,
        2,
    )