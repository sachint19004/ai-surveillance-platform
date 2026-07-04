from pydantic import BaseModel, EmailStr, Field


class AccountCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8)


class AccountResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str
    is_active: bool

    model_config = {
        "from_attributes": True
    }


class AccountLogin(BaseModel):
    email: EmailStr
    password: str