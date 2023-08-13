#!/usr/bin/python3
"""
BaseModel module:
BaseModel that defines all\
common attributes/methods\
for other classes
id: string - assign with an\
uuid when an instance is created
created_at: datetime - assign\
with the current datetime\
when an instance is created
updated_at: datetime - assign\
with the current datetime\
when an instance is created and it will be updated
"""
import uuid
from datetime import datetime as dt
from models import storage


class BaseModel:

    """
    BaseModel that defines all common\
    attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
            Public instances attributes:
            id: unique identifier for instances in string data type
            created_at: datetime of creation
            updated_at: datetime of update
        """
        if (kwargs == {}):
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if (key == "__class__"):
                    continue
                setattr(self, key, dt.fromisoformat(value)
                        if ("_at" in key) else value)

    def __str__(self):
        """
            String representation of class
        """
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
            updates the public instance\
            attribute updated_at with the current datetime
        """
        self.updated_at = dt.now()
        storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all\
            keys/values of __dict__ of the instance
        """
        obj_dict = {}

        for key, value in self.__dict__.items():
            obj_dict[key] = value.isoformat() if ("_at" in key) else value
        obj_dict["__class__"] = type(self).__name__

        return (obj_dict)
