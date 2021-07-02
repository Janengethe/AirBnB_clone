#!/usr/bin/python3
"""
Tests for City class
"""

import unittest
import os
import pep8
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.my_city = City()
        #cls.my_city.name = "Nairobi"
        #cls.my_city.state_id = "Nbi"

    @classmethod
    def tearDownClass(cls):
        del cls.my_city
        try:
            os.remove("BaseModel.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        """
        Tests City inherits from BaseModel
        """
        self.assertTrue(issubclass(self.my_city.__class__, BaseModel), True)

    def test_funcs(self):
        """
        Tests documentations
        """
        self.assertIsNotNone(City.__doc__)

    def test_attributes(self):
        """
        Tests attributes in the class
        """
        self.assertTrue('id' in self.my_city.__dict__)
        self.assertTrue('created_at' in self.my_city.__dict__)
        self.assertTrue('updated_at' in self.my_city.__dict__)
        #self.assertTrue('state_id' in self.my_city.__dict__)
        #self.assertTrue('name' in self.my_city.__dict__)

    def test_attributes_are_strings(self):
        """
        Tests attributes are str
        """
        self.assertEqual(type(self.my_city.name), str)
        self.assertEqual(type(self.my_city.state_id), str)

if __name__ == "__main__":
    unittest.main()
