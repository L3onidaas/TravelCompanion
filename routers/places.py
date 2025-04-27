from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud import save_place
from services.service import result_place


router = APIRouter()


@router.get('/places/')
def places(place: str, city: str, db: Session = Depends(get_db)):

    all_places = result_place(place, city)

    for new_place in all_places:
        save_place(new_place, db)


    return "Успешно, проверь запись в базе данных"