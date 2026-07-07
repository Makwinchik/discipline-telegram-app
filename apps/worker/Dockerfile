FROM python:3.12-slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg libgl1 && rm -rf /var/lib/apt/lists/*
COPY apps/api/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY apps/api/app /app/app
COPY apps/worker/pipeline /app/pipeline
CMD ["celery", "-A", "app.services.tasks.celery_app", "worker", "--loglevel=INFO"]
