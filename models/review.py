#!/usr/bin/python3
""" Class review that inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ Class Review that inherits from BaseModel """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(self, *args, **kwargs)
