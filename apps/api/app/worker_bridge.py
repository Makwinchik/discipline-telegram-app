from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.domain import Clip, Video, VideoStatus
from app.services.ai_pipeline import analyze_video

def run_pipeline(video_id: str) -> dict:
    db: Session = SessionLocal()
    try:
        video = db.get(Video, video_id)
        if not video:
            return {"error": "not_found"}
        result = analyze_video(video.source_key)
        video.transcript = result["transcript"]
        video.analysis = result["analysis"]
        video.status = VideoStatus.rendered
        for item in result["clips"]:
            db.add(Clip(video_id=video.id, **item))
        db.commit()
        return {"status": "rendered", "clips": len(result["clips"])}
    except Exception as exc:
        if 'video' in locals() and video:
            video.status = VideoStatus.failed
            db.commit()
        raise exc
    finally:
        db.close()
