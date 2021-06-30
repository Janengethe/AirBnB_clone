#!/usr/bin/python3
"""
Module file_storage
Serializes instances to a JSON file and
Deserializes JSON file to instances
Has private class attributes __file_path, __objects
"""


import os
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Private class attribute declaration
    """
    __file_path = "BaseModel.json"
    __objects = {}
    all_classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                   'City': City, 'Amenity': Amenity, 'Place': Place,
                   'Review': Review}

    def all(self):
        """
        The getter-> return ojects stored in __objects.
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        setter->
        sets in __objects the obj with key "<obj class name>.id"
        """
        if obj is None:
            return
        key = obj.__class__.__name__ + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes dict __objects to JSON file
        """
        my_dict = {}
        for key, obj in FileStorage.__objects.items():
            my_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to dict __objects
        It only load if the file exists, else pass
        if os.path.exists(FileStorage.__file_path):
        """
        try:
            with open(FileStorage.__file_path, mode="r") as f:
                reloaded_dict = json.load(f)
                for k, v in reloaded_dict.items():
                    base = FileStorage.all_classes[v["__class__"]](**v)
                    FileStorage.__objects[k] = base
        except FileNotFoundError:
            pass
