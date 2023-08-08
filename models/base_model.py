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
            return (f"[<{self.__class__.name}>] (<{self.id}>) <{self.__dict__}>")
        
        def save(self):
            """
                updates the public instance attribute updated_at with the current datetime
            """
            self.updated_at = dt.now()

        def to_dict(self):
            """
               returns a dictionary containing all keys/values of __dict__ of the instance 
            """

            CpyObj = self.__dict__.copy() # a copy of __dict__
            CpyObj['__class__'] = self.__class__.__name__
            CpyObj['created_at'] = self.created_at.isoformat()
            CpyObj['updated_at'] = self.updated_at.isoformat()
            return (CpyObj)

        



