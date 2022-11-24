#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        @property
        def cities(self):
            """Getter of cities"""
            from models import storage
            from models.city import City
            list_city = []
            for city in storage.all(City):
                if self.id == city.state_id:
                    list_city.append(city)
            return list_city 
