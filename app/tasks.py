import time

from app.celery_app import celery_app


@celery_app.task(track_started=True)
def background_task():
    time.sleep(10)
    return "Task completed!"
