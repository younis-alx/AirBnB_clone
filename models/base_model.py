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
        from models import storage 
        if kwargs:

            kwargs["created_at"] = dt.strptime(
                                               kwargs["created_at"],
                                               "%Y-%m-%dT%H:%M:%S.%f"
                                   )
            kwargs["updated_at"] = dt.strptime(
                                               kwargs["updated_at"],
                                               "%Y-%m-%dT%H:%M:%S.%f"
                                   )

            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            storage.new(self)

    def __str__(self):
        """
            String representation of class
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
            updates the public instance\
            attribute updated_at with the current datetime
        """
        from models import storage
        self.updated_at = dt.now()
        storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all\
            keys/values of __dict__ of the instance
        """

        cpy_obj = self.__dict__.copy()  # a copy of __dict__
        cpy_obj['__class__'] = self.__class__.__name__
        cpy_obj['created_at'] = self.created_at.isoformat()
        cpy_obj['updated_at'] = self.updated_at.isoformat()
        return cpy_obj
