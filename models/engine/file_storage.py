#!/usr/bin/python3
"""
FileStorage that serializes instances to a\
JSON file and deserializes JSON file to instances
"""
import json
from os.path import isfile


class FileStorage:
    """
        class that serializes instances\
        to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return (FileStorage.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        objects = {}
        for key, value in FileStorage.__objects.items():
            objects[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            file.write(json.dumps(objects))

    def reload(self):
        """
        Deserializes the JSON file to __objects\
        if the file exists; otherwise, do nothing.
        """
        objects = {}

        if (isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as file:
                objects = json.loads(file.read())
            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.amenity import Amenity
            from models.city import City
            from models.place import Place
            from models.review import Review
            for key, value in objects.items():
                class_name = value["__class__"]
                del value["__class__"]
                FileStorage.__objects[key] = eval(class_name + "(**value)")
