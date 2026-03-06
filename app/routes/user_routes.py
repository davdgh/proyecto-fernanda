from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user_model import User
from typing import List, Optional
from app.utils.security import hash_password
from app.schemas.user_schema import UserResponse, UserUpdate
from app.schemas.user_schema import LoginRequest
from app.utils.security import verify_password
from app.utils.jwt_handler import create_access_token

router = APIRouter()

@router.get("/users", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

# ENDPOINT PARA ACTUALIZAR USUARIO
@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    if user_data.email is not None:
        user.email = user_data.email

    if user_data.password is not None:
        user.password = hash_password(user_data.password)

    if user_data.role is not None:
        user.role = user_data.role

    db.commit()
    
    db.refresh(user)

    return user

