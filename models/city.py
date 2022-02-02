#!/usr/bin/python3
""" Class city that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """ Class State  that inherits from BaseModel"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(self, *args, **kwargs)
