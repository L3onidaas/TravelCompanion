from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud import save_place
from services.service import result_place


places_router = APIRouter()


@places_router.get('/places/')
def places(place: str, city: str, db: Session = Depends(get_db)) -> str:
    """Функция для получения и записи мест в БД"""

    all_places = result_place(place, city)

    for new_place in all_places:
        save_place(new_place, db)


    return "Успешно, проверь запись в базе данных"