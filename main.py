from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import engine, get_db
from services.service import result_place
from crud import save_place, save_user



models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.post("/users/")
def create_user(user: schemas.Users, db: Session = Depends(get_db)):

    save_user(user, db)

    return "Успешно, проверь запись в базе данных"


@app.get('/places/')
def places(place: str, city: str, db: Session = Depends(get_db)):

    all_places = result_place(place, city)

    for new_place in all_places:
        save_place(new_place, db)


    return "Успешно, проверь запись в базе данных"

