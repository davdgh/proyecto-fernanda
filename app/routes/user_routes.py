from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user_model import User
from typing import List
from app.schemas.user_schema import UserResponse

router = APIRouter()

@router.get("/users", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):

    users = db.query(User).all()
    return users