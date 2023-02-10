#!/usr/bin/python3
"""
Filestorage module
"""
import json


class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances"""
    # Added private class attributes to the __init__ method
    def __init__(self, __file_path, __objects):
        self.__file_path = __file_path
        self.__objects = __objects

    def all(self):
        return self.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        return FileStorage.__objects

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

