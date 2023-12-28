#!/usr/bin/python3
"""
Handles the database storage and interactions (ORM) using SQLAlchemy """
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from os import getenv


class DBStorage:
    """ DBStorage class for database storage """
    __engine = None
    __session = None

    def __init__(self):
        """ Create a new DBStorage instance """
        user = getenv("HBNB_MYSQL_USER")
        passwrd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        # Create an engine and connect to the database
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(user, passwrd, host, db), pool_pre_ping=True)
        # Drop all tables if the environment variable HBNB_ENV is equal to test
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query the current database """
        dict = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.quey(cls)
            for item in query:
                key = "{}.{}".format(type(item).__name__, item.id)
                dict[key] = item
        else:
            list_args = [State, City, User, Place, Review, Amenity]
            for name in list_args:
                query = self.__session.query(name)
                for item in query:
                    key = "{}.{}".format(type(item).__name__, item.id)
                    dict[key] = item
        return dict

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database and create the current database session """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """ 
        Calls remove()
        """
        self.__session.close()
