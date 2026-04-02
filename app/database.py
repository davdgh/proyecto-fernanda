from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.utils.logger import logger

DATABASE_URL = "sqlite:///./users2.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def get_db():
    logger.info("Se entro a la función para crear la conexión a la base de datos")
    logger.debug("BD status: creating")
    db = SessionLocal()
    try:
        logger.info("Se creó con éxito la conexión base de datos")
        logger.debug("BD status: created")
        yield db
    except Exception as e:
        logger.error("Ocurrió un error al crear la conexión a la base de datos")
        logger.debug(f"BD status: refused, reason: {e}")
        raise
    finally:
        logger.info("Se cerró la conexión a la base de datos")
        logger.debug("BD status: closed")
        db.close()
