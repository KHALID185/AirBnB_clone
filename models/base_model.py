#!/usr/bin/python3
"""Module base_model
Defines a class that serves as a base for other classes,
providing common attributes and methods.
"""
from uuid import uuid4
from datetime import datetime
from models import storage
import json
import sys
import os.path


class BaseModel():
    '''A base class for other classes'''

    def __init__(self, *args, **kwargs):
        '''
        values initialization
        '''
        if kwargs:
            date_format = '%Y-%m-%dT%H:%M:%S.%f'
            attributes = kwargs.copy()
            del attributes["__class__"]
            for attribute in attributes:
                if attribute in ("created_at", "updated_at"):
                    attributes[attribute] = datetime.strptime(attributes[attribute], date_format)
            self.__dict__ = attributes
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''
        Returns a string representation of the instance.
        Format: "[<class name>] (<self.id>) <self.__dict__>"
        '''
        return '[{}] ({}) {}'.format(
                self.__class__.__name__,
                self.id,
                self.__class__.__dict__))

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''
        Returns a dictionary containing all keys 
        and values of the instance's __dict__.
        '''
        result_dict = {}
        result_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                result_dict[key] = value.isoformat()
            else:
                result_dict[key] = value
        return result_dict

    def to_json(self):
        '''
        Returns a JSON string representation of the instance.
        '''
        json_dict = self.__dict__.copy()
        json_dict.update({'created_at': self.created_at.strftime(self.date_format)})
        json_dict.update({'__class__': str(self.__class__.__name__)})
        if hasattr(self, 'updated_at'):
            json_dict.update({'updated_at': self.updated_at.strftime(self.date_format)})
        return json_dict
