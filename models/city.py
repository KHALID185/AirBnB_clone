#!/usr/bin/python3
from models.base_model import BaseModel
"""Module: City - Defines the City class"""


class City(BaseModel):
    """Represents a City.

        Attributes:
        name (str): The name of the city.
        state_id (str): The ID of the state associated with the city.
    """
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """initialization using constructor"""
        super().__init__(self, *args, **kwargs)
