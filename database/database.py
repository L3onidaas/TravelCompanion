from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import os
from typing import Generator


load_dotenv()
database_url = os.getenv("database_url")


engine = create_engine(database_url, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    """Функция создания подключения к БД"""

    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()