from datetime import datetime

from pydantic import BaseModel, ConfigDict


class KnownFaceCreate(BaseModel):
    name: str
    employee_id: str
    department: str


class KnownFaceResponse(BaseModel):
    id: int
    name: str
    employee_id: str
    department: str
    image_path: str
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)