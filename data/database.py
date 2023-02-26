from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings


engine = create_engine(settings.DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()