#!/usr/bin/python3
"""
creating a unique FileStorage instance for our  application

Storage object
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
