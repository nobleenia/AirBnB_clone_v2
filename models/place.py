#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
import models


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey("places.id"), primary_key=True, nullable=False),
                      Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan', backref="place")
        amenities = relationship('Amenity', secondary=place_amenity, viewonly=False, back_populates='place_amenities')
    else:
        @property
        def reviews(self):
            """ Returns list of reviews.id """
            var = models.storage.all()
            list_args = []
            result = []
            for key in var:
                review = key.replace('.', ' ')
                review = shlex.split(review)
                if (review[0] == 'Review'):
                    list_args.append(var[key])
            for item in list_args:
                if (item.place_id == self.id):
                    result.append(item)
            return (result)

        @property
        def amenities(self):
            """ Returns the amenities list """
            all_amenities = models.storage.all(Amenity)
            place_amenities = []
            for amenity_ins in all_amenities.values():
                if amenity_ins.place_id == self.id:
                    place_amenities.append(amenity_ins)
            return place_amenities

        @amenities.setter
        def amenities(self, obj=None):
            """ Appends amenity ids to the attribute """
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
