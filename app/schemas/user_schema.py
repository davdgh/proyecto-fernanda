from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=10)

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    password: str

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None