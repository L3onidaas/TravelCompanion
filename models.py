from sqlalchemy import Column, String, Integer, Float
from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    city = Column(String, index=True)


class Place(Base):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    city = Column(String)


