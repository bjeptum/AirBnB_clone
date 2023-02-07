#!/usr/bin/python3
"""
Filestorage module
"""


class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances"""
    def __init__(self):
        self.__file_path = __file_path
        self.__objects = __objects

    def all(self):
        return self. __objects
    
    def new(self, obj):
        """Sets in __objects"""
        
