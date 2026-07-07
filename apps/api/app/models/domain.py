import enum
import uuid
from datetime import datetime
from sqlalchemy import DateTime, Enum, Float, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.session import Base

class VideoStatus(str, enum.Enum):
    uploaded = "uploaded"
    analyzing = "analyzing"
    clipping = "clipping"
    rendered = "rendered"
    failed = "failed"

class Video(Base):
    __tablename__ = "videos"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    owner_id: Mapped[str] = mapped_column(String(128), index=True)
    title: Mapped[str] = mapped_column(String(255))
    source_key: Mapped[str] = mapped_column(String(512))
    duration_seconds: Mapped[int | None] = mapped_column(Integer)
    status: Mapped[VideoStatus] = mapped_column(Enum(VideoStatus), default=VideoStatus.uploaded)
    transcript: Mapped[str | None] = mapped_column(Text)
    analysis: Mapped[dict | None] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    clips: Mapped[list["Clip"]] = relationship(back_populates="video")

class Clip(Base):
    __tablename__ = "clips"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    video_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("videos.id"), index=True)
    title: Mapped[str] = mapped_column(String(255))
    topic: Mapped[str] = mapped_column(String(160))
    score: Mapped[float] = mapped_column(Float)
    duration_seconds: Mapped[int] = mapped_column(Integer)
    output_key: Mapped[str | None] = mapped_column(String(512))
    captions: Mapped[dict | None] = mapped_column(JSON)
    hashtags: Mapped[dict | None] = mapped_column(JSON)
    description: Mapped[str | None] = mapped_column(Text)
    video: Mapped[Video] = relationship(back_populates="clips")
