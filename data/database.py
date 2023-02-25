from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Settings


@lru_cache()
def get_settings():
    return Settings()


engine = create_engine(Settings().DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()