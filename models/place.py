#!/usr/bin/python3
"""Defines a Module for the class Place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class definition for Place.


    Attributes:
        city_id (str): The city id.
        user_id (str): The user's id.
        name (str): The name of the place.
        description (str): A description of the place.
        number_rooms (int): The number of rooms.
        number_bathrooms (int): The number of bathrooms.
        max_guest (int): The maximum number of guests allowed.
        price_by_night (int): The price per night.
        latitude (float): The latitude.
        longitude (float): The longitude.
        amenity_ids (list): A list of Amenities by id.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
