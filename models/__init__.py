#!/usr/bin/python3
"""
This module is executed when the models package is imported.
It initializes the storage system and loads any existing data from storage.
"""
from models.engine.file_storage import FileStorage
# Create an instance of FileStorage

storage = FileStorage()

# Load any existing data from storage

storage.reload()
