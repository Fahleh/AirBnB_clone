#!/usr/bin/python3
"""This module instantiates the models directory as a Python package"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
