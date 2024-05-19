#!/usr/bin/python3
from models.base_model import BaseModel
from models.place import Place
from models.user import User
"""
    review module class
"""


class Review(BaseModel):
    """la definition of the reviw class"""
    text = ""
    place_id = ""
    user_id = ""

    def __init__(self, *args, **kwargs):
        """initialization using constractor"""
        super().__init__(self, *args, **kwargs)
