#!/usr/bin/python3

import cmd
import uuid
from datetime import datetime as dt

class BaseModel:
    
    """BaseModel that defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """
            Public instances attributes:
            id: unique identifier for instances in string data type
            created_at: datetime of creation
            updated_at: datetime of update
        """
        self.id = str(uuid.uuid4())
        self.created_at = dt.now()
        self.updated_at = dt.now()

        def __str__(self):
            """
                String representation of class
            """
            return f"[<{self.__class__.name}>] (<{self.id}>) <{self.__dict__}>"
        


