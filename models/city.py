#!/usr/bin/python3
"""Defines a module for a class  City"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Defines the class City.

    Attributes:
        state_id (str): The id of the state.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
