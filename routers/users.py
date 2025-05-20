from fastapi import APIRouter, Depends
from schemas import schemas
from sqlalchemy.orm import Session
from crud.crud import save_user
from database.database import get_db


users_router = APIRouter()


@users_router.post("/users/")
def create_user(user: schemas.Users, db: Session = Depends(get_db)) -> str:
    """Функция для получения и записи пользователей в БД"""

    save_user(user, db)

    return "Успешно, проверь запись в базе данных"