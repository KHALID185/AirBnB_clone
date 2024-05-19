#!/usr/bin/python3
"""
    user class in model
"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    '''le module de base de user class'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
