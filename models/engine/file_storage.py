#!/usr/bin/python3
"""
Filestorage module
"""
import json


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
<<<<<<< HEAD
        return self.__objects
=======
        """Returns the dictionaries"""
        return (FileStorage.__objects)
>>>>>>> 80e497fb9f2e3a4e5a6663791e4a58cbd982ca17
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        pass

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage._file_path, "w", encoding="utf-8") as f:
            json.dump(f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists\
                ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""
        if not os.path.isfile(FileStorage._file_path):
            return
        with open(FileStorage._file__file_path, "r", encoding="utf-8") as f:

