from fastapi import APIRouter, Depends
import schemas
from sqlalchemy.orm import Session
from crud import save_user
from database import get_db


router = APIRouter()


@router.post("/users/")
def create_user(user: schemas.Users, db: Session = Depends(get_db)):

    save_user(user, db)

    return "Успешно, проверь запись в базе данных"