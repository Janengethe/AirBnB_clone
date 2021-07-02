#!/usr/bin/python3
import os
import json
import unittest
from models.user import User
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


""" Testing instantiation"""
class TestFileStorage(unittest.TestCase):
    def test_class_has_attributes_type(self):
      file1 = FileStorage()
      self.assertTrue(hasattr(FileStorage, "all"))
      self.assertTrue(hasattr(FileStorage, "new"))
      self.assertTrue(hasattr(FileStorage, "save"))
      self.assertTrue(hasattr(FileStorage, "reload"))
      self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))
      self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))
      self.assertTrue(hasattr(file1, "all"))
      self.assertTrue(hasattr(file1, "new"))
      self.assertTrue(hasattr(file1, "save"))
      self.assertTrue(hasattr(file1, "reload"))
      self.assertTrue(type(file1.all), dict)
      self.assertFalse(hasattr(file1, "__file_path"))
      with self.assertRaisesRegex(AttributeError, "'FileStorage' object has no attribute '_TestFileStorage__objects'"):
            type(file1.__objects) == dict
      with self.assertRaisesRegex(AttributeError, "'FileStorage' object has no attribute '_TestFileStorage__file_path'"):
            type(file1.__file_path) == str

    def test_private_attribute(self):
        with self.assertRaises(AttributeError):
            FileStorage.__file_path
            Filetorage.__objects

    def test_all(self):
      file2 = FileStorage()
      i = file2.all()
      self.assertIsNotNone(i)
      self.assertIsInstance(i, dict)
      self.assertEqual(type(i), dict)
      self.assertIs(i, file2._FileStorage__objects)
      """for k, v in i.items():
          for q, j in v.items():
              self.assertIn(q, ["id", "created_at", "updated_at", "__class__"])
      """

    def test_new(self):
        """
        Tests method: new (saves object into dictionary)
        """
        n_storage = FileStorage()
        dic = n_storage.all()
        rev = User()
        rev.id = 5437
        rev.name = "Jane"
        n_storage.new(rev)
        key = rev.__class__.__name__ + "." + str(rev.id)
        self.assertIsNotNone(dic[key])

    def test_save_reload(self):
        """Tests save and reload method"""
        base2 = BaseModel()
        base_s = base2.save()
        self.assertTrue(os.path.isfile('BaseModel.json'))
        tmp_obj = BaseModel()
        tmp_id = 'BaseModel.' + tmp_obj.id
        tmp_obj.save()
        del storage._FileStorage__objects[tmp_id]
        storage.reload()
        self.assertIn(tmp_id, storage.all())

if __name__ == "__main__":
    unittest.main()
