#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv as env


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if env("HBNB_TYPE_STORAGE") == db:
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        kwargs = {"cascade": "all, delete-orphan", "backref": "user"}
        places = relationship("Place", **kwargs)
        reviews = relationship("Review", **kwargs)
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
