#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref='state', cascade="all, delete",
                              passive_deletes=True)

    @property
    def cities(self):
        """Getter of cities"""
        list_city = []
        for city in storage.all(City):
            if self.id == city.state_id:
                list_city.append(city)
        return list_city
