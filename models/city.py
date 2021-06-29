#!/usr/bin/python3
"""
Module city defines a class City that inherits from BaseModel
Public class attributes:
                   name: string - empty string
                   state_id: string - empty string: it will be the State.id
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    Class City inherits from BaseModel
    Public class attributes:
                       name: string - empty string
                       state_id: string - empty string: it will be the State.id
    """
    name = ""
    state_id = ""
