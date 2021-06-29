#!/usr/bin/python3
"""
Module test_base_model
Contains the test cases for module base_model
"""


from models.engine.file_storage import FileStorage
from datetime import datetime
import unittest
from models.base_model import BaseModel
import models


class TestBaseModel(unittest.TestCase):
    """
    Testing instantiation
    """
    def test_init_type(self):
        """
        Tests initialization of base_model attributes
        """
        my_model = BaseModel()
        my_model.name = "Jane"
        my_model.my_number = 89
        self.assertTrue(type(my_model), BaseModel)
        self.assertTrue(type(my_model.id), str)
        self.assertTrue(type(my_model.created_at), datetime)
        self.assertTrue(type(my_model.updated_at), datetime)
        self.assertTrue(my_model.name, "Jane")

    def test_isinstance(self):
        """
        Tests class BaseModel instances added
        """
        my_model = BaseModel()
        my_model.name = "Jane"
        my_model.my_number = 89
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(isinstance(my_model, BaseModel))

    def test_kwargs(self):
        """
        Tests keyward arguments used
        """
        my_model = BaseModel()
        a_dict = my_model.to_dict()
        base1 = BaseModel(a_dict)
        self.assertIsNotNone(base1.id)
        self.assertTrue(type(base1.id), str)
        self.assertTrue(type(base1.created_at), datetime)
        self.assertTrue(type(base1.created_at), datetime)
        self.assertTrue(type(base1), BaseModel)

    def test_isinstance_base1(self):
        """
        Tests class BaseModel instances
        """
        my_model = BaseModel()
        a_dict = my_model.to_dict()
        base1 = BaseModel(a_dict)
        self.assertIsInstance(base1, BaseModel)
        self.assertTrue(isinstance(base1, BaseModel))

    def test_str(self):
        """
        Tests method __str__ used in base_model
        """
        base2 = BaseModel()
        self.assertIn("id", base2.__str__())
        self.assertIn("created_at", base2.__str__())
        self.assertIn("updated_at", base2.__str__())
        self.assertIn("[BaseModel]", base2.__str__())
        self.assertTrue(type(base2.__str__()), str)
        self.assertIsNotNone(base2.__str__())

    def test_save(self):
        """
        Tests method save
        """
        base3 = BaseModel()
        self.assertNotEqual(base3.created_at, base3.updated_at)
        update1 = base3.updated_at
        base3.save()
        update2 = base3.updated_at
        self.assertNotEqual(update1, update2)

    def test_to_dict(self):
        """
        Tests method to_dict
        """
        base4 = BaseModel()
        self.assertTrue(type(base4.to_dict()), dict )
        self.assertIn("id", base4.to_dict())
        self.assertIn("__class__", base4.to_dict())
        self.assertIn("updated_at", base4.to_dict())
        self.assertIn("created_at", base4.to_dict())

    def test_attributes(self):
        """
        Tests class attributes prsent in module base_model
        """
        base5 = BaseModel()
        self.assertIn("to_dict", dir(base5))
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "__repr__"))

    def test_funcs(self):
        """
        Tests functions contents
        """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

if __name__ == "__main__":
    unittest.main()
