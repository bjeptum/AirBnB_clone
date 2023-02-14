#!/usr/bin/python3
"""A module that creates a user class"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class for managing amenity objects"""

    name = ""
