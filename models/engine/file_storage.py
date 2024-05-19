#!/usr/bin/python3
import os.path
import json
import os

"""
Module file_storage
Contains a class FileStorage
that serializes instances to a JSON file and
deserializes JSON file to instances
"""

class FileStorage():
    """
        Manages storage of objects by serializing to and deserializing
        from JSON files.
    """

    # Initializing file path and objects dictionary
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects containing all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to __objects with the key format <obj class name>.id.
        """
        if obj:
            # Constructs the key and stores the object
            #in __objects if the object exists
            name = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[name] = obj

    def save(self):
        """
        Serializes __objects to a JSON file specified by __file_path.
        """
        dic = {}

        for ky, vl in self.__objects.items():
            # Serializes each object using its key
            dic[ky] = vl.to_dict()

        with open(self.__file_path, "w") as my_file:
            json.dump(dic, my_file)

    def reload(self):
        """
        Deserializes the JSON file to __objects if the file exists.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        # Mapping of class names to their corresponding classes
        dic = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

        if not os.path.isfile(self.__file_path):
            return

        with open(self.__file_path, "r") as file_path:
            objects = json.load(file_path)
            self.__objects = {}
            for ky in objects:
                # Retrieves class name from key and creates an inst
                name = ky.split(".")[0]
                self.__objects[ky] = dic[name](**objects[ky])
