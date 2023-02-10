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
        # the object type = self.__class__.__name__
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        # Create a new dictionary from the object stored in FileStorage.__objects dict
        # The new dict contains key-value pairs, where the key is the same as the FileStorage.__objects dict
        # The result is a dict, with the same key as FileStorage.__objects dict
        # but with vaues converted to dict
        my_json_dict = {}
        for key, value in FileStorage.__objects.items():
            my_json_dict[key] = value.to_dict()
        with open(FileStorage._file_path, "w", encoding="utf-8") as f:
            json.dump(my_json_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists\
                ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""
        # if not os.path.isfile(FileStorage._file_path)
        if (exists(FileStorage.__file_path)):
            # checks if the file exists, opens it, and loads the JSON data
            with open(FileStorage._file__file_path, "r", encoding="utf-8") as f:
                my_obj = json.load(f)
                # iterate through the values of the JSON and sets class name and values
                for value in my_obj.values():
                    class_name = value['__class__name']
                    del value['__class__']
                    # remove class key and create a new instance of the class and pass the values as key args
                    self.new(eval(class_name)(**value))

