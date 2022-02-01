#!/usr/bin/python3
"""
file_storage model that serializes python objects and deserialize json files
"""


import json
from models.base_model import BaseModel


class FileStorage:
    """
    class FileStorage that serializes instances to a JSON file and\
     deserializes JSON file to instances.

    Attributes
    ----------
    __file_path : str
        path to the JSON file

    __objects : dictionary
        empty but will store all objects by <class name>.id

    Methods
    -------
    all(self):
        returns the dictionary __objects

    new(self, obj):
        sets in __objects the obj with key <obj class name>.id
    save(self):
        serializes __objects to the JSON file (path: __file_path)
    reload(self):
         deserializes the JSON file to __objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        name_id = obj.__class__.__name__ + "." + str(obj.id)
        self.__object[name_id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file\
         (__file_path) exists ; otherwise, do nothing. If the file\
        doesn’t exist, no exception should be raised
       """

        try:
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                # jlo = json.load(f)
                for key, value in json.load(f).items():
                    attri_value = eval(value["__class__"])(**value)
                    self.__objects[key] = attri_value
        except FileNotFoundError:
            pass
