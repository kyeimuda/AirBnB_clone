#!/usr/bin/python3
"""Contains modules for the BaseModel class"""


import uuid
import models
from datetime import datetime


class BaseModel:
    """
    Creates the class 'BsaeModel' that defines all common\
     attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """ Constructor """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()
                    models.storage.new(self)

    def __str__(self):
        """representation of a string"""
        return "[{}] ({}) {}".format(self.__class__, self.id, self.__dict__)

    def save(self):
        """Updates public instance attribute with the current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all key values of  an instance"""
        dict_copy = self.__dict__
        dict_copy["__class__"] = self.__class__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
