import json

class FileStorage:
    """
        class that serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_key = str(obj.__class__.__name__) + '.' + str(obj.id)
        val_dict = obj
        FileStorage.__objects[obj_key] = val_dict

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        
        obj_dict = {}
        
        for key, val in FileStorage.__objects.items():
            obj_dict[key] = val.to_dict()
        
        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as json_file:
           json.dump(obj_dict,json_file)

    def reload(self):
        """Deserializes the JSON file to __objects if the file exists; otherwise, do nothing."""
        from models.base_model import BaseModel

        try:
            with open(FileStorage.__file_path, encoding="UTF8") as json_file:
                obj_dict = json.load(json_file)
            for key, val in obj_dict.items():
                FileStorage.__objects[key] = BaseModel(**val)
        except FileNotFoundError:
            pass