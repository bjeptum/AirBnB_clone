#!/usr/bin/python3
"""
Base module
"""


class BaseModel:
    """ Defines all common attributes/methods for other classes"""
    def __init__(self, id = None):
        self.id = id

    def save(self):
        """Updates insatnce attribute with the current datetime"""
        pass

    def to_dict(self):
        """ Returns all keys/values of __dict__ of the instance"""
        retuen self.__dict__

