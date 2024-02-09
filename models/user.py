#!/usr/bin/python3
"""This module defines a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class definition for User.

    Attributes:
        email (str): The user's email.
        password (str): The user's password.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
