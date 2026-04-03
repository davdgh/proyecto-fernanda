from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user_model import User
from app.schemas.user_schema import UserRegister
from app.utils.security import hash_password
from app.schemas.user_schema import LoginRequest
from app.utils.security import verify_password
from app.utils.jwt_handler import create_access_token
from app.utils.logger import logger

router = APIRouter()

@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    logger.info("Se entró a la ruta de registro")

    if not user.email or not user.password:
        logger.debug("ENDPOINT: /register, Info: Correo o contraseña no pasadas al body, se rechaza la creación de usuario")
        logger.warning(f"No se pasó el correo o la contraseña")
        raise HTTPException(status_code=400, detail="Correo y contraseña son necesarios")

    # Verificar email existente
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        logger.debug("ENDPOINT: /register, Info: Correo ya existente, se rechaza la creación de nuevo usuario")
        logger.warning(f"El correo: '{user.email}' ya se encuentra en la base de datos")
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

    logger.info("Usuario creado con éxito")
    return {"message": "Usuario registrado correctamente"}

# ENPOINT PARA LOGIN
@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    logger.info("Se entró al endpoint de login")
    user = db.query(User).filter(User.email == data.email).first()

    if not user:
        logger.debug(f"ENDPOINT: /login, Info: No se encontró ningún usuario con el correo: '{data.email}'")
        logger.warning("Correo no encontrado en la base de datos")
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    if not verify_password(data.password, user.password):
        logger.debug("ENDPOINT: /login, Info: La contraseña especificada no coincide con la que se encuentra en la base datos")
        logger.warning("Contraseñas distintas")
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    token = create_access_token({
        "sub": str(user.id),
        "email": user.email
    })
    logger.info("JWT creado con éxito")

    return {
        "access_token": token,
        "token_type": "bearer"
    }