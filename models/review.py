#!/usr/bin/python3
"""Defines a module defines a class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class definition for Review

    Attributes:
        place_id (str): The id of the place.
        user_id (str): The user's id.
        text (str): The content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
