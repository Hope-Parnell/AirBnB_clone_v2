#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models.user import User
import os


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    place_id = Column(String(60), ForeignKey('places.id'),
                      nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'),
                     nullable=False)
    text = Column(String(1024), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def user(self):
            """gets the user who made the review"""
            from models import storage
            return storage.all(User).get("User.{}".format(self.user_id))
