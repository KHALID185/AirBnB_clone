#!/usr/bin/python3
from models.base_model import BaseModel
"""
place -- module class
"""


class Place(BaseModel):
    """place class definition"""
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longtude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initialization using constractor"""
        super().__init__(self, *args, **kwargs)
