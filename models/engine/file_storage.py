"""A module implementing a file storage class model"""

import json

from models.base_model import BaseModel


class FileStorage:
    """
    A class that serializes instances to JSON files,
    and deserializes JSON files to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the `obj` with key <obj class name>.id."""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, "w") as fd:
            storage_obj = {}
            for key, value in self.__objects.items():
                storage_obj[key] = value.to_dict()
            json.dump(storage_obj, fd)

    def reload(self):
        """
        Deserializes the JSON file to __objects ONLY IF it exists!
        If the file doesn’t exist, no exception should be raised.
        """
        modules = {'BaseModel': BaseModel}
        try:
            with open(self.__file_path, 'r') as fd:
                temp = json.load(fd)
            for key in temp:
                self.__objects[key] = modules[temp[key]["__class__"]](**temp[key])
        except FileNotFoundError:
            pass
