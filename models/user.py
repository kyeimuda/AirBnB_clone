#!/usr/bin/python3
""" A class named user that inherits from BaseModell"""

from models.base_model import BaseModel


class User(BaseModel):
    """ Class user that inherits from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
