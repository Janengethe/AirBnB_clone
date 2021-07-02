#!/usr/bin/python3
""" Tests class User"""

import unittest
import os
import pep8
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.my_user = User()
        cls.my_user.first_name = "Jane"
        cls.my_user.last_name = "Keira"
        cls.my_user.email = "janekeira@gmail.com"
        cls.my_user.password = "missjane"

    @classmethod
    def tearDownClass(cls):
        del cls.my_user
        try:
            os.remove("BaseModel.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        """
        Tests user inherits from BaseModel
        """
        self.assertTrue(issubclass(self.my_user.__class__, BaseModel), True)

    def test_isinstance(self):
        """
        Check that the created instance is an instance of the BaseModel class
        """
        self.assertIsInstance(self.my_user, BaseModel)

    def test_funcs(self):
        """
        Tests documentations
        """
        self.assertIsNotNone(User.__doc__)

    def test_attributes(self):
        """
        Tests attributes in the class
        """
        self.assertTrue('email' in self.my_user.__dict__)
        self.assertTrue('id' in self.my_user.__dict__)
        self.assertTrue('created_at' in self.my_user.__dict__)
        self.assertTrue('updated_at' in self.my_user.__dict__)
        self.assertTrue('password' in self.my_user.__dict__)
        self.assertTrue('first_name' in self.my_user.__dict__)
        self.assertTrue('last_name' in self.my_user.__dict__)

    def test_they_exists(self):
        """
        Tests that the attributes exists
        """
        self.assertTrue(hasattr(User, 'email'))
        self.assertTrue(hasattr(User, 'password'))
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertTrue(hasattr(User, 'last_name'))

    def test_their_types(self):
        """
        Test that all attributes are of the correct type
        """
        self.assertTrue(type(self.my_user), BaseModel)

    def test_str_attributes(self):
        """
        Tests attributes are strings
        """
        self.assertEqual(type(User.email), str)
        self.assertEqual(type(User.password), str)
        self.assertEqual(type(User.first_name), str)
        self.assertEqual(type(User.last_name), str)

if __name__ == "__main__":
    unittest.main()
