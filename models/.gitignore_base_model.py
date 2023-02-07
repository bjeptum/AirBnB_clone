#!/usr/bin/python3
"""
Base model
"""
import uuid
import datetime


class BaseModel:
    """Defines all common attributes/methods of other classes."""
    def __init__(self, id, created_at, updated_at):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Should print [<class name>] (<self.id>) <self.__dict__>"""
        print("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__")

    def save(self):
        """Updates instance attribute with the current datetime"""
        self.update_at = datetime.now()

    def to_dict(self):
        """Returns all keys/values of __dict__ of the instance"""
        pass

    """
    def __init__(self, *args, **kwargs):
    """Update the base model using *args, **kwargs arguments for the constructor of BaseModel"""
    if kwags is not empty:
        if key == "created_at":
        # convert to datetime object
        """
        datetime.strptime(created_at, %Y-%m-%dT%H:%M:%S.%f)
        datetime.strptime(updated_at, %Y-%m-%dT%H:%M:%S.%f)
        """
    elif key == "updates_at":
        #convert to datetime object
    else:
        self.id = str(uuid.uuid())
        self.created_at = datetime.now()
    """
