from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from enum import Enum

class RoleEnum(str, Enum):
    cliente = 'cliente'
    teacher = 'teacher'
    student = 'student'

class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=10)
    role: RoleEnum = RoleEnum.cliente

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    password: str
    role: RoleEnum

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    email: Optional[str] = EmailStr
    password: Optional[str] = Field(min_length=8, max_length=10)
    role: Optional[RoleEnum]

class LoginRequest(BaseModel):
    email: str
    password: str