import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True) 
    name = Column(String(250), nullable=False)
    email= Column(String(250), nullable=False)
    constraseña= Column(String(250), nullable=False)
    username= Column(String(250), nullable=False)

class Favorite(Base):
    __tablename__ = 'Favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey('User.id'), nullable=False)
    characters_id = Column(Integer, ForeignKey('Characters.id'), nullable=True)
    planets_id = Column(Integer, ForeignKey('Planets.id'), nullable=True)

class Characters(Base):
    __tablename__='Characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    age = Column(Integer, nullable=False)

class Planets(Base):
    __tablename__='Planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=True)
    diameter = Column(Integer, nullable=True)
    rotation = Column(Integer, nullable=True)
    gravity = Column(String(250), nullable=True)
    population = Column(Integer, nullable=True)
    climate = Column(String(250), nullable=True)
    terrain = Column(String(250), nullable=True)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
