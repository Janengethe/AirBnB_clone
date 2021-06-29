#!/usr/bin/python3
"""
Module base_model
has class BaseModel that defines all
common atributes/methods for other classes
"""


import models
import uuid
from datetime import datetime


class BaseModel:
    """
    public instance attributes:
    id, created_at, updated_at
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization
        id uses uuid.uuid4(). Regenerates a unique id for each BaseModel.
        updated_at -> datetime will be updated everytime an object is changed.
        *args and **kwargs are used as constructors
        """
        if kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            for k, v in kwargs.items():
                if kwargs[k] == "id":
                    self.id = v
                elif kwargs[k] == "created_at":
                    self.created_at = datetime.strptime(v,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif kwargs[k] == "updated_at":
                    self.updated_at = datetime.strptime(v,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    pass
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns string rep of class BaseModel
        Prints: "[<class name>] (<self.id>) <self.__dict__>"
        """
        print("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        """
        Returns the string representation of BaseModel
        calls __str__()
        """
        return (self.__str__())

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        Calls save(self) method of storage
        """
        models.storage.new(self.to_dict())
        models.storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__.__name__
        for k, v in my_dict.items():
            if my_dict[k] == "id":
                my_dict[k] = v

            elif isinstance(v, datetime):
                my_dict[k] = v.isoformat()
            else:
                my_dict[k] = v
        return my_dict
