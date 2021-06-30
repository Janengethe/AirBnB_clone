#!/usr/bin/python3
"""
Module state defines a class User that inherits from BaseModel
Public class attributes:
                   name: string - empty string
"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    Class State inherits from BaseModel
    Public class attributes:
                       name: string - empty string
    """
    name = ""
