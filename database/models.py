from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column
from database.database import Base


class User(Base):
    __tablename__ = 'users'

    id = mapped_column(Integer, primary_key=True, index=True)
    name = mapped_column(String, index=True)
    city = mapped_column(String, index=True)
    email = mapped_column(String, index=True)


class Place(Base):
    __tablename__ = 'places'

    id = mapped_column(Integer, primary_key=True, index=True)
    name = mapped_column(String)
    address = mapped_column(String)
    city = mapped_column(String)


