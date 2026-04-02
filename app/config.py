import os
from dotenv import load_dotenv
from app.utils.logger import logger

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

    def __init__(self):
        if self.SECRET_KEY is None:
            message = "No se encontró la variable 'SECRET_KEY' dentro del archivo '.env'"
            logger.warning(message)
            raise Exception(message)
