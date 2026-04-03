from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user_model import User
from typing import List
from app.utils.security import hash_password
from app.schemas.user_schema import UserResponse, UserUpdate
from app.utils.logger import logger

router = APIRouter()

@router.get("/users", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    logger.info("Se entró al endpoint para conseguir a todos los usuarios existentes")
    users = db.query(User).all()
    logger.info("Se recuperaron todos los usuarios con éxito")
    return users

@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    logger.info("Se entró al endpoint de obtener usuario por su id")
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        logger.debug(f"ENDPOINT: /users/{user_id}, METHOD: GET, Info: No se encontró ningún usuario con el id: '{user_id}'")
        logger.warning("No se encontró ningún usuario con el id")
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    logger.info("Usuario recuperado con éxito")
    return user

# ENDPOINT PARA ACTUALIZAR USUARIO
@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    logger.info("Se entró al endpoint de actualizar usuario")
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        logger.debug(f"ENDPOINT: /users/{user_id}, METHOD: PUT, Info: No se encontró ningún usuario con el id: '{user_id}'")
        logger.warning("No se encontró ningún usuario con el id")
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    if user_data.email is not None:
        logger.info("Se busca actualizar el correo, guardando el nuevo correo")
        user.email = user_data.email

    if user_data.password is not None:
        logger.info("Se busca actualizar la contraseña, hasheando la nueva contraseña")
        user.password = hash_password(user_data.password)

    if user_data.role is not None:
        logger.info("Se busca actualizar el rol, guardando el nuevo rol")
        user.role = user_data.role

    db.commit()

    db.refresh(user)

    logger.info("Usuario actualizado con éxito")
    return user