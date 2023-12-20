#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models import storage

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan', backref="state")

    @property
    def cities:
        """ Getter attribute that returns the list of City instances
               with state_id equals to the current State.id"""
        cities_list = []
        stored_data = storage.all(City).items()
        for city_id, city in stored_data:
            try:
                if city.state_id == self.id:
                    cities_list.append(city)
            except Exception:
                pass
        return cities_list
