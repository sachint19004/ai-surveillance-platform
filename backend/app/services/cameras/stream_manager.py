import cv2


class CameraManager:

    def __init__(self):
        self.streams = {}

    def open_camera(
        self,
        camera_id: int,
        source: str,
    ):
        if camera_id in self.streams:
            return self.streams[camera_id]

        try:
            source = int(source)
        except ValueError:
            pass

        capture = cv2.VideoCapture(source)

        if not capture.isOpened():
            raise RuntimeError("Unable to open camera")

        self.streams[camera_id] = capture

        return capture

    def get_frame(
        self,
        camera_id: int,
    ):
        capture = self.streams.get(camera_id)

        if capture is None:
            raise RuntimeError("Camera not opened")

        success, frame = capture.read()

        if not success:
            raise RuntimeError("Unable to read frame")

        return frame

    def release_camera(
        self,
        camera_id: int,
    ):
        capture = self.streams.pop(
            camera_id,
            None,
        )

        if capture:
            capture.release()


camera_manager = CameraManager()