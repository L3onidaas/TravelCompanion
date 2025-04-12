from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal
import requests
from creds import api_token, url


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/")
def create_user(user: schemas.Users, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name, city=user.city)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return "Успешно, проверь запись в базе данных"


@app.get('/places/')
def places(place: str, city: str, db: Session = Depends(get_db)):
    params = {
        'query': place,
        'near': city,
        'limit': 10,
    }
    headers = {
        'Authorization': api_token,
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()

        for place in data['results']:
            name = place['name']
            location = place['location']
            address = location.get('address', 'Адрес не указан')

            new_places = {'name': name, 'address': address}

            db_place = models.Place(name=new_places['name'], address=new_places['address'], city=city)
            db.add(db_place)
            db.commit()
            db.refresh(db_place)


        return "Успешно, проверь запись в базе данных"

    else:
         return f'Ошибка {response.status_code}'
