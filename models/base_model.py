#!/usr/bin/python3
"""
Base module
"""

import uuid
import datetime
import models


class BaseModel:
    """ Defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """ Recreate instance variables of the dict representation"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.datetime.strptime
                            (value, "%Y-%m-%dT%H:%M:%S.%f"))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns string representation of instance"""
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates instance attribute with the current datetime"""
        self.updated_at = datetime.datetime.now()
        # call save(self) method of storage
        models.storage.save()

    def to_dict(self):
        """ Returns all keys/values of __dict__ of the instance"""
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.__dict__['created_at'].isoformat()
        new_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        return (new_dict)
