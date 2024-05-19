#!/usr/bin/python3
from models.base_model import BaseModel
"""Represents an Amenity.

Attributes:
    name (str): The name of the amenity.
"""


class Amenity(BaseModel):
    """Represents an Amenity."""
    name = ""  # The name of the amenity

    def __init__(self, *args, **kwargs):
        """Initializes a new Amenity instance"""
        super().__init__(*args, **kwargs)
