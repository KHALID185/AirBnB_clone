#!/usr/bin/python3
from models.base_model import BaseModel
"""
State module class
"""


class State(BaseModel):
    """ la definition de state class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialization using constructor"""
        super().__init__(self, *args, **kwargs)
