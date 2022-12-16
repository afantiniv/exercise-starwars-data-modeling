import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable=False)
    email = Column(String(350),nullable=False)


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable = False)
    rotation_period = Column(Integer, nullable = False)
    orbital_period = Column(Integer, nullable = False)
    population = Column(Integer, nullable = False)
    surface_water = Column(Integer, nullable = False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    eyes_color = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    birthday = Column(String(250), nullable=False)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets, backref= 'planets')

class Fav_planets(Base):
    __tablename__ = 'fav_planets'
    id = Column(Integer, primary_key=True)
    user_id = (Column(Integer, ForeignKey('user.id')))
    user = relationship(User, backref= 'user')
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets, backref= 'planets')

class Fav_characters(Base):
    __tablename__ = 'fav_characters'
    id = Column(Integer, primary_key = True)
    user_id = (Column(Integer, ForeignKey('user.id')))
    user = relationship(User, backref= 'user')
    characters_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship(Characters, backref= 'characters')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
