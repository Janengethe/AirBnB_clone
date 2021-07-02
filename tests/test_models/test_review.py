#!/usr/bin/python3
""" Tests Review class """

import unittest
import os
import pep8
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.my_rev = Review()
        #cls.my_rev.place_id = "Westlands"
        #cls.my_rev.user_id = "Jane0015"
        #cls.my_rev.text = "A***"

    @classmethod
    def tearDownClass(cls):
        del cls.my_rev
        try:
            os.remove("BaseModel.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        """
        Tests Review inherits from BaseModel
        """
        self.assertTrue(issubclass(self.my_rev.__class__, BaseModel), True)

    def test_funcs(self):
        """
        Tests __doc__
        """
        self.assertIsNotNone(Review.__doc__)

    def test_attributes(self):
        """
        Tests class attributes
        """
        self.assertTrue('id' in self.my_rev.__dict__)
        self.assertTrue('created_at' in self.my_rev.__dict__)
        self.assertTrue('updated_at' in self.my_rev.__dict__)
        #self.assertTrue('place_id' in self.my_rev.__dict__)
        #self.assertTrue('text' in self.my_rev.__dict__)
        #self.assertTrue('user_id' in self.my_rev.__dict__)

    def test_str_attributes(self):
        self.assertEqual(type(self.my_rev.text), str)
        self.assertEqual(type(self.my_rev.place_id), str)
        self.assertEqual(type(self.my_rev.user_id), str)

if __name__ == "__main__":
    unittest.main()
