#!/usr/bin/python3
""" Class definition of a city """
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State

Base = declarative_base()


class City(Base):
    """City class that inherits from Base"""
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
