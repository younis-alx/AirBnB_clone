#!/usr/bin/python3

import cmd
import uuid
from datetime import datetime as dt

class BaseModel:
    
    """BaseModel that defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = dt.now()
        self.updated_at = dt.now()

