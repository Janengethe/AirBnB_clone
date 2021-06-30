#!/usr/bin/python3
"""
Module review defines a class Review  that inherits from BaseModel
Public class attributes:
                   place_id: string - empty string
                   user_id: string - empty string: it will be the State.id
                   text: string, empty string
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class Review inherits from BaseModel
    Public class attributes:
                   place_id: string - empty string
                   user_id: string - empty string: it will be the State.id
                   text: string, empty string

    """
    place_id = ""
    user_id = ""
    text = ""
