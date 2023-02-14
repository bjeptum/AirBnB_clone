#!/usr/bin/python3
"""
Filestorage module
"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        # the object type = self.__class__.__name__
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        # Create a new dictionary from the object stored in
        # FileStorage.__objects dict
        # The new dict contains key-value pairs, where the key
        # is the same as the FileStorage.__objects dict
        # The result is a dict, with the same key as FileStorage.__objects dict
        # but with vaues converted to dict
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict().copy()
            with open(FileStorage.__file_path, "w", encoding="utf-8") as ofile:
                json.dump(new_dict, ofile)

    def reload(self):
        """deserializes the JSON file """
        try:
            with open(FileStorage.__file_path, 'r') as ofile:
                new_dict = json.load(ofile)
                for key, value in new_dict.items():
                    class_name = value.get('__class__')
                    obj = eval(class_name + '(**value)')
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
