#!/usr/bin/python3
"""A module implementing the Base class"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    A class that defines all the attributes and
    methods common to the other classes.
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            del kwargs["__class__"]
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            self.__dict__.update(kwargs)
        else:
            from models import storage
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns the string representation of BaseModel object as:
        [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the attribute 'self.updated_at' with the current datetime"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of
        the instance:
               - Only instance attributes set will be returned.
               - A key __class__ is added with the class name of the object.
               - created_at and updated_at must be converted to string object
                 in ISO format.
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                value = self.__dict__[key].isoformat()
                new_dict[key] = value
        return new_dict
