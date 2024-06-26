#!/usr/bin/python3
""" Amenity class."""

from sqlalchemy import Column
from sqlalchemy import String
from models.base_model import BaseModel, Base
from models.base_model import BaseModel
from models.place import place_amenity
from sqlalchemy.orm import relationship


class Amenity (BaseModel, Base):
   """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
