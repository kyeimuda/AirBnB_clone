#!/usr/bin/python3
"""unittest for BaseModel"""

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """ Unittest for BaseModel class"""
    
    def test_id(self):
        """testing to check if self.id is no equal """
        test_try2 = BaseModel()
        test_try1 = BaseModel()
        self.assertNotEqual(test_try2.id, test_try1.id)

    def test_init_BaseModel(self):
        """testing to check if an object is of type BaseModel"""
        test_try = BaseModel()
        self.assertIsInstance(test_try, BaseModel)

    def test_str(self):
        """testing to check if __str__ returns the rigth string format"""
        test_try = BaseModel()
        string1 ="[{}] ({}) {}".format(test_try.__class__.__name__, self.id, self.__dict__)
        string2 = str(my_strobject)
        self.assertEqual(string1, string2)
