#!/usr/bin/python3
"""This module creates a user class"""


from models.base_model import BaseModel


class City(BaseModel):
    """class for managing city objects"""

    state_id = ""
    name = ""
