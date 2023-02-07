#!/usr/bin/python3
"""
Base module
"""

import uuid
import datetime



class BaseModel:
    """ Defines all common attributes/methods for other classes"""
    def i__init__(self, id, created_at, updated_at):
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
        dict = self.__dict__.copy
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return dict
