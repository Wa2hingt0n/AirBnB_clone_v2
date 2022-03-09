#!/usr/bin/python3
""" Handles the database storage engine for all instances """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship


class DBStorage:
    """ Defines methods for handling database storage of instances """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializes the database engine """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"), getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ Queries the current database session all objects depending on
            class name. If cls=None all objects (User, State, City, Amenity
            Place and Review) are queried.

        Args:
            cls: The class to be queried
        """
        if cls is None:
            instances = self.__session.query(
                User, State, City, Amenity, Place, Review).all()
        else:
            if type(cls) == str:
                cls = eval(cls)
            instances = self.__session.query(cls)

        instance_dict = {}
        for obj in instances:
            key = "{}:{}".format(type(obj).__name__, obj.id)
            instance_dict[key] = obj

        return (instance_dict)

    def new(self, obj):
        """ Adds obj to the current database session

        Args:
            obj: Object to be added to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """ Commits all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes an object(obj) from the current database session if
            it exists

        Args:
            obj: Object to be deleted.
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """ Creates all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ Closes an SQLAlchemy session """
        self.__session.close()
