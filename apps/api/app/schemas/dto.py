from uuid import UUID
from pydantic import BaseModel, Field

class UploadIntent(BaseModel):
    filename: str
    content_type: str
    size_bytes: int = Field(le=5 * 1024 * 1024 * 1024)

class UploadIntentResponse(BaseModel):
    video_id: UUID
    upload_url: str
    object_key: str

class ClipRead(BaseModel):
    id: UUID
    title: str
    topic: str
    score: float
    duration_seconds: int
    output_url: str | None = None
    hashtags: dict | None = None
    description: str | None = None
    model_config = {"from_attributes": True}

class VideoRead(BaseModel):
    id: UUID
    title: str
    status: str
    duration_seconds: int | None
    analysis: dict | None = None
    clips: list[ClipRead] = []
    model_config = {"from_attributes": True}
