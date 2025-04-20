import models
from sqlalchemy.orm import Session
import schemas


def save_place(new_places, db: Session):
    db_place = models.Place(name=new_places['name'], address=new_places['address'], city=new_places['city'])
    db.add(db_place)
    db.commit()
    db.refresh(db_place)

    return db_place


def save_user(user: schemas.Users, db: Session):
    db_user = models.User(name=user.name, city=user.city)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user