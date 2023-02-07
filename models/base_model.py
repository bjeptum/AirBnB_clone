#!/usr/bin/python3
"""
Base module
"""

import uuid
import datetime



class BaseModel:
    """ Defines all common attributes/methods for other classes"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at= datetime.datetime.now()

    def __str__(self):
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)
        

    def save(self):
        """Updates instance attribute with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ Returns all keys/values of __dict__ of the instance"""
        return self.__dict__
