import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload
from app.db.session import get_db
from app.models.domain import Clip, Video, VideoStatus
from app.schemas.dto import UploadIntent, UploadIntentResponse, VideoRead
from app.services.storage import StorageService

router = APIRouter(prefix="/api/v1")

@router.get("/health")
def health():
    return {"status": "ok", "service": "clipforge-api"}

@router.post("/uploads/intent", response_model=UploadIntentResponse)
def create_upload_intent(payload: UploadIntent, db: Session = Depends(get_db)):
    video = Video(owner_id="demo-user", title=payload.filename, source_key=f"uploads/{uuid.uuid4()}-{payload.filename}")
    db.add(video)
    db.commit()
    db.refresh(video)
    upload_url = StorageService().presigned_put(video.source_key, payload.content_type)
    return UploadIntentResponse(video_id=video.id, upload_url=upload_url, object_key=video.source_key)

@router.post("/videos/{video_id}/process")
def process_video(video_id: uuid.UUID, db: Session = Depends(get_db)):
    video = db.get(Video, video_id)
    if not video:
        raise HTTPException(404, "Video not found")
    video.status = VideoStatus.analyzing
    db.commit()
    from app.services.tasks import process_video_task
    process_video_task.delay(str(video_id))
    return {"queued": True, "video_id": video_id}

@router.get("/videos", response_model=list[VideoRead])
def list_videos(db: Session = Depends(get_db)):
    return db.query(Video).options(selectinload(Video.clips)).order_by(Video.created_at.desc()).all()

@router.get("/videos/{video_id}", response_model=VideoRead)
def get_video(video_id: uuid.UUID, db: Session = Depends(get_db)):
    video = db.query(Video).options(selectinload(Video.clips)).filter(Video.id == video_id).first()
    if not video:
        raise HTTPException(404, "Video not found")
    return video

@router.delete("/clips/{clip_id}")
def delete_clip(clip_id: uuid.UUID, db: Session = Depends(get_db)):
    clip = db.get(Clip, clip_id)
    if not clip:
        raise HTTPException(404, "Clip not found")
    db.delete(clip)
    db.commit()
    return {"deleted": True}
