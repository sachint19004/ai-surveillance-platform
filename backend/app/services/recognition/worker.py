import threading
import time

from sqlalchemy.orm import Session

from app.services.cameras.stream_manager import camera_manager
from app.services.recognition.recognizer import recognize_frame


class RecognitionWorker:

    def __init__(self):
        self.workers = {}

    def start(
        self,
        camera_id: int,
        db_factory,
    ):
        if camera_id in self.workers:
            return

        stop_event = threading.Event()

        thread = threading.Thread(
            target=self.run,
            args=(
                camera_id,
                db_factory,
                stop_event,
            ),
            daemon=True,
        )

        self.workers[camera_id] = (
            thread,
            stop_event,
        )

        thread.start()

    def stop(
        self,
        camera_id: int,
    ):
        worker = self.workers.pop(
            camera_id,
            None,
        )

        if worker:
            worker[1].set()

    def run(
        self,
        camera_id,
        db_factory,
        stop_event,
    ):
        while not stop_event.is_set():

            db: Session = db_factory()

            try:

                frame = camera_manager.get_frame(camera_id)

                face, score = recognize_frame(
                    db,
                    frame,
                )

                if face:

                    print(
                        f"[Camera {camera_id}] "
                        f"{face.name} "
                        f"({score:.3f})"
                    )

            except Exception as e:

                print(e)

            finally:

                db.close()

            time.sleep(0.2)


recognition_worker = RecognitionWorker()