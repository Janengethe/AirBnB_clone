#!/usr/bin/python3
from models.base_model import BaseModel
from datetime import datetime
import json
from models.engine.file_storage import FileStorage
import os
import unittest


""" Testing instantiation"""
class TestFileStorage(unittest.TestCase):
    def test_class_has_attributes_type(self):
      file1 = FileStorage()
      self.assertTrue(hasattr(FileStorage, "all"))
      self.assertTrue(hasattr(FileStorage, "new"))
      self.assertTrue(hasattr(FileStorage, "save"))
      self.assertTrue(hasattr(FileStorage, "reload"))
      self.assertTrue(hasattr(file1, "all"))
      self.assertTrue(hasattr(file1, "new"))
      self.assertTrue(hasattr(file1, "save"))
      self.assertTrue(hasattr(file1, "reload"))
      self.assertTrue(type(file1.all), dict)
      self.assertFalse(hasattr(file1, "__file_path"))
      with self.assertRaisesRegex(AttributeError, "'FileStorage' object has no attribut\
e '_TestFileStorage__objects'"):
            type(file1.__objects) == dict
      with self.assertRaisesRegex(AttributeError, "'FileStorage' object has no attribut\
e '_TestFileStorage__file_path'"):
            type(file1.__file_path) == str

    def test_private_attribute(self):
        with self.assertRaises(AttributeError):
            FileStorage.__file_path
            Filetorage.__objects

    def test_all(self):
      file2 = FileStorage()
      i = file2.all()
      self.assertIsNotNone(i)
      self.assertTrue(type(i), dict)
      for k, v in i.items():
          self.assertIn(["id", "created_at", "updated_at", "__class__"], v)

    def test_new(self):
        file3 = FileStorage()
        base1 = BaseModel()
        obj = base1.to_dict()
        file3.new(obj)
        ke_y = obj["__class__"] + "." + obj["id"]
        all_objects = file3.all()
        self.assertIn(ke_y, all_objects)
        self.assertIsNotNone(all_objects[ke_y])
        self.assertNotEqual("{}", all_objects[ke_y])

    def test_save_reload(self):
        file4 = FileStorage()
        with open("BaseModel.json", mode="w") as f:
            f.write("{}")
        with open("BaseModel.json", mode="r") as fl:
            for line in fl:
                self.assertEqual(line, "{}")
        self.assertIs(file4.reload(), None)
