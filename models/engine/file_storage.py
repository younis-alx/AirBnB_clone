import json

class FileStorage:
    """
        class that serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = ""
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_key = str(obj.___class___.___name___) + '.' + str(obj.id)

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as json_file:
           json.dump(FileStorage.__objects,json_file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(FileStorage.__file_path, mode='r', encoding="UTF8") as obj:
                FileStorage.__objects = json.load(obj)
        except FileNotFoundError:
            pass