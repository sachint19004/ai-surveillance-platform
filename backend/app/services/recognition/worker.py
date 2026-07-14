import threading
import time

from sqlalchemy.orm import Session

from app.services.cameras.stream_manager import camera_manager
from app.services.recognition.recognizer import recognize_frame
from app.services.events.service import log_recognition_event


class RecognitionWorker:

    def __init__(self):
       self.workers = {}

        # stores last logged time
       self.last_events = {}

        # seconds before same event is allowed again
       self.event_interval = 10

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
    def should_log_event(
        self,
        camera_id: int,
        face,
    ):
        """
        Returns True only if enough time has passed
        since this face was last logged.
        """

        if face:

            key = (
                camera_id,
                f"KNOWN_{face.id}",
            )

        else:

            key = (
                camera_id,
                "UNKNOWN",
            )

        current_time = time.time()

        last_time = self.last_events.get(
            key,
            0,
        )

        if current_time - last_time < self.event_interval:

            return False

        self.last_events[key] = current_time

        return True

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

                if self.should_log_event(
                    camera_id,
                    face,
                ):

                    log_recognition_event(
                        db=db,
                        camera_id=camera_id,
                        face=face,
                        score=score,
                    )

                if face:

                    print(
                        f"[Camera {camera_id}] "
                        f"{face.name} "
                        f"({score:.3f})"
                    )

                else:

                    print(
                        f"[Camera {camera_id}] "
                        f"UNKNOWN"
                    )

            except Exception as e:

                print(e)

            finally:

                db.close()

            time.sleep(0.2)


recognition_worker = RecognitionWorker()