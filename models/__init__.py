#!/usr/bin/python3
"""
Module __init__
Creates a unique FileStorage instance
"""


from models.engine import file_storage
from models.base_model import BaseModel

storage = file_storage.FileStorage()
storage.reload()
