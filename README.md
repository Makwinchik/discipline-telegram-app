# ClipForge AI

Production-ready SaaS scaffold for converting long-form videos into viral vertical shorts with AI analysis, captioning, editing, and exports.

## Stack

- Frontend: Next.js, TypeScript, TailwindCSS, shadcn-style components, Framer Motion-ready structure
- Backend: FastAPI, PostgreSQL, Redis, Celery, S3-compatible storage, JWT/OAuth-ready auth
- AI pipeline: FFmpeg, Whisper, Pyannote, OpenCV, MediaPipe, YOLO/GPT integration seams

## Quick start

```bash
cp .env.example .env
docker compose up --build
```

Services:

- Frontend: http://localhost:3000
- API: http://localhost:8000/docs
- PostgreSQL: localhost:5432
- Redis: localhost:6379
- MinIO: http://localhost:9001

## Architecture

```text
apps/web          Next.js dashboard, upload, review, editor, exports
apps/api          FastAPI app, auth, videos, clips, exports, billing
apps/worker       Celery worker and AI/video processing pipeline
packages/shared   Shared TypeScript contracts and constants
infra             Database migrations and deployment notes
```

The pipeline is intentionally modular. Heavy AI integrations are wrapped behind services so production deployments can swap local models, managed GPU workers, or vendor APIs without changing API contracts.
