#!/usr/bin/python3

"""Defines the City class."""
from models.base_model import Base
from models.base_model import BaseModel
from models.place import Place
from sqlalchemy import Column, Foreignkey, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class City(BaseModel, Base):
    """Represents a city for a MySQL database.
    Attributes:
        __tablename__ : The name of the MySQL table to store Cities.
        name : The name of the City.
        state_id : The state id of the City.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete, all, delete-orphan")
