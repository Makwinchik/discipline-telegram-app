from celery import Celery
from app.core.config import settings

celery_app = Celery("clipforge", broker=settings.celery_broker_url, backend=settings.celery_result_backend)

@celery_app.task(name="process_video")
def process_video_task(video_id: str):
    from app.worker_bridge import run_pipeline
    return run_pipeline(video_id)
