#!/usr/bin/python3
"""This module defines for database storage"""
from sqlalchemy import create_engine, MetaData
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from os import getenv


class DBStorage:
    """Database storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Creates engine connection"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      getenv("HBNB_MYSQL_USER"),
                                      getenv("HBNB_MYSQL_PWD"),
                                      getenv("HBNB_MYSQL_HOST"),
                                      getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

	if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary represent of the query"""
        new = {}    

    def new(self, obj):
        """Adds the object to the current database session"""


    def save(self):
        """Commits all changes of the current database session"""


    def delete(self, obj=None):
        """Deletes from the current database session"""


    def reload(self):
        """Creates all tables in the database"""

    def close(self):
        """Closes a session"""
