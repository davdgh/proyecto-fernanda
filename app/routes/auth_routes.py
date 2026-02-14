from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user_model import User
from app.schemas.user_schema import UserRegister
from app.utils.security import hash_password

router = APIRouter()

@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):

    # Verificar email existente
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="El correo ya está registrado")

    # Hashear contraseña
    hashed_password = hash_password(user.password)

    # Crear usuario
    new_user = User(
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "Usuario registrado correctamente"}
