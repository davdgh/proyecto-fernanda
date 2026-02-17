from fastapi import FastAPI
from app.database import engine, Base
from app.routes.auth_routes import router as auth_router
from app.routes.user_routes import router as user_router

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)

app.include_router(user_router)
