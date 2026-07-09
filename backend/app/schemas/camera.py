from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CameraCreate(BaseModel):
    name: str
    location: str
    source: str


class CameraUpdate(BaseModel):
    name: str
    location: str
    source: str


class CameraResponse(BaseModel):
    id: int
    name: str
    location: str
    source: str
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)