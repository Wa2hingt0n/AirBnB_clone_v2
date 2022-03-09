#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")

    else:
        name = ""

        @property
        def cities(self):
            """ Returns the list of City instances where
                state_id == current State.id
            """
            city_dict = models.storage.all(City)
            city_list = []
            for city in city_dict.values():
                if city.state_id == self.id:
                    city_list.append(city)

            return city_list
