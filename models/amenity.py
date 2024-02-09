#!/usr/bin/python3
"""Defines a module defines a class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class definition for Amenitty.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""
