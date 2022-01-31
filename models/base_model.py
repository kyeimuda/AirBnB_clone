 #!/usr/bin/python3
"""Contains modules for the BaseModel class"""
  
from uuid import uuid4
from datetime import datetime
from models

class BaseModel:
    """
    Creates the class 'BsaeModel' that defines all common\
     attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            self.id = kwargs['id']
            self.created_at = datetime.strptime(kwargs
                                                ['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            self.update_at = datetime.strptime(kwargs
                                                 ['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
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
 

