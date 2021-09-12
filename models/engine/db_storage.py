#!/usr/bin/python3
'''manages DBstorage'''
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from sqlalchemy import create_engine
from models.base_model import Base
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place
from models.user import User
from models.city import City
from os import getenv as env


class DBStorage():
    '''manages mysql database with sqlalchemy'''
    __engine = None
    __session = None

    def __init__(self):
        '''initializes'''
        usr = env("HBNB_MYSQL_USER")
        passwd = env("HBNB_MYSQL_PWD")
        host = env("HBNB_MYSQL_HOST")
        db = env("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(usr, passwd, host, db),
                                      pool_pre_ping=True)
        if env("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''returns the dict of all objs'''
        dict_all = {}
        list_object = []
        if cls:
            list_object = self.__session.query(cls).all()
        else:
            classList = [Amenity, Review, State, Place, User, City]
            for cs in classList:
                list_object += self.__session.query(cs)
        for obj in list_object:
            key = "{}.{}".format(obj.__class__.__name__, str(obj.id))
            dict_all[key] = obj
        return dict_all

    def new(self, obj):
        '''adds a new object to the session'''
        self.__session.add(obj)

    def save(self):
        '''commits session to the database'''
        self.__session.commit()

    def delete(self, obj=None):
        '''deletes an object from current session'''
        self.__session.delete(obj)

    def reload(self):
        '''reloads the engine session and objs'''
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(expire_on_commit=False, bind=self.__engine)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        """Remove private session attribute"""
        self.__session.close()
