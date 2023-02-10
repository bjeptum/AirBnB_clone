#!/usr/bin/python3
"""
Filestorage module
"""


import json
from models.base_model import BaseModel

class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances
    The abstracted storage module"""
    # Added private class attributes to the __init__ method
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionaries"""
        return (FileStorage.__objects)
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        pass

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        pass

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists\
                ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""
        pass
