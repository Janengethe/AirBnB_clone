#!/usr/bin/python3
""" Tests city class """

import unittest
import os
import pep8
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.my_place = Place()
        #cls.my_place.city_id = "Rwaka"
        #cls.my_place.user_id = "rwaka0015"
        #cls.my_place.name = "Two rivers"
        #cls.my_place.description = "Pride of Kenya"
        #cls.my_place.number_rooms = 0
        #cls.my_place.number_bathrooms = 0
        #cls.my_place.max_guest = 0
        #cls.my_place.price_by_night = 0
        #cls.my_place.latitude = 0.0
        #cls.my_place.longitude = 0.0
        #cls.my_place.amenity_ids = []

    @classmethod
    def tearDownClass(cls):
        del cls.my_place
        try:
            os.remove("BaseModel.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        """
        Tests Place inherits from BaseModel
        """
        self.assertTrue(issubclass(self.my_place.__class__, BaseModel), True)

    def test_funcs(self):
        """
        Tests documentations
        """
        self.assertIsNotNone(Place.__doc__)

    def test_attributes(self):
        """
        Tests attributes in class Place
        """
        self.assertTrue('id' in self.my_place.__dict__)
        self.assertTrue('created_at' in self.my_place.__dict__)
        self.assertTrue('updated_at' in self.my_place.__dict__)
        #self.assertTrue('city_id' in self.my_place.__dict__)
        #self.assertTrue('user_id' in self.my_place.__dict__)
        #self.assertTrue('name' in self.my_place.__dict__)
        #self.assertTrue('description' in self.my_place.__dict__)
        #self.assertTrue('number_rooms' in self.my_place.__dict__)
        #self.assertTrue('number_bathrooms' in self.my_place.__dict__)
        #self.assertTrue('max_guest' in self.my_place.__dict__)
        #self.assertTrue('price_by_night' in self.my_place.__dict__)
        #self.assertTrue('latitude' in self.my_place.__dict__)
        #self.assertTrue('longitude' in self.my_place.__dict__)
        #self.assertTrue('amenity_ids' in self.my_place.__dict__)

    def test_strintfloatlist_attributes(self):
        """
        Tests attributes are str int float and list
        """
        self.assertEqual(type(self.my_place.city_id), str)
        self.assertEqual(type(self.my_place.user_id), str)
        self.assertEqual(type(self.my_place.name), str)
        self.assertEqual(type(self.my_place.description), str)
        self.assertEqual(type(self.my_place.number_rooms), int)
        self.assertEqual(type(self.my_place.number_bathrooms), int)
        self.assertEqual(type(self.my_place.max_guest), int)
        self.assertEqual(type(self.my_place.price_by_night), int)
        self.assertEqual(type(self.my_place.latitude), float)
        self.assertEqual(type(self.my_place.longitude), float)
        self.assertEqual(type(self.my_place.amenity_ids), list)

if __name__ == "__main__":
    unittest.main()
