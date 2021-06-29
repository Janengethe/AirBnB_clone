#!/usr/bin/python3
"""
Module file_storage
Serializes instances to a JSON file and
Deserializes JSON file to instances
Has private class attributes __file_path, __objects
"""


import os
import json


class FileStorage:
    """
    Private class attribute declaration
    """
    __file_path = "BaseModel.json"
    __objects = {}

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
        if obj == {} or obj is None:
            return
        key = obj["__class__"] + "." + obj["id"]
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes dict __objects to JSON file
        """
        if FileStorage.__objects is None or FileStorage.__objects == {}:
            pass

        my_dict = {}
        for k, v in self.__objects.items():
            my_dict[k] = v
        with open(FileStorage.__file_path, mode="w", encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to dict __objects
        It only load if the file exists, else pass
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode="r") as f:
                FileStorage.__objects = json.load(f)
        else:
            pass
