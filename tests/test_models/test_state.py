#!/usr/bin/python3
"""
Tests class State
"""

import unittest
import os
import pep8
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.my_state = State()

    @classmethod
    def tearDownClass(cls):
        del cls.my_state
        try:
            os.remove("BaseModel.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        """
        Tests State inherits from BaseModel
        """
        my_state = State()
        self.assertTrue(issubclass(self.my_state.__class__, BaseModel), True)

    def test_funcs(self):
        """
        Tests method __doc__
        """
        self.assertIsNotNone(State.__doc__)

    def test_attributes(self):
        """
        Tests attributes in the class
        """
        self.assertTrue('id' in self.my_state.__dict__)
        self.assertTrue('created_at' in self.my_state.__dict__)
        self.assertTrue('updated_at' in self.my_state.__dict__)
        #self.assertTrue('name' in self.my_state.__dict__)

    def test_str_attributes(self):
        """
        Tests attributes are strings
        """
        self.assertEqual(type(self.my_state.name), str)

if __name__ == "__main__":
    unittest.main()
