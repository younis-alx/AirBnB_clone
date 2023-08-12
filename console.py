#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        """quite the program"""

        return True
    
    def do_EOF(self, line):
        """Exit the program"""
        print()
        return True
    
    def emptyline(self):
        """Do nothing on empty line"""
        pass
    
    def do_create(self, line):
        """create: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel"""
        
        if len(line) == 0:
            print("** class name missing **")
            return
        try:
             line = line.split()
             new_instances = eval(line[0])()
             new_instances.save()
             print(new_instances.id)
        except:
             print("** class doesn't exist **")


    def do_show(self, line): #TODO refactor if have time
        """Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234."""
        if len(line) == 0:
            print("** class name missing **")
            return
        line = line.split()
        if len(line) == 1:
            print("** instance id missing")
            return
        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        try:
             eval(line[0])
        except NameError:
             print("** class doesn't exist **")
             return
        key = line[0] + "." + line[1]
        try:
            value = obj_dict[key]
            print(value)
        except KeyError:
            print("** no instance found **")
            return

        
    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234."""
        line = line.split()
        if len(line) == 0:
            print("** class name missing **")
            return
        elif len(line) == 1:
            print("** instance id missing **")
            return
        class_name = line[0]
        class_id = line[1]
        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        try:
            eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        key = class_name + "." + class_id
        try:
            del obj_dict[key]
        except KeyError:
            print("** no instance found **")
        storage.save()

    
    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all."""
        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        obj_list = []
        line = line.split()

        try:
            if line and not eval(line[0]):
                print("** class doesn't exist **")
            elif not line:
                for val in objects.values():
                    obj_list.append(str(val))
            else:
                for val in objects.values():
                    if line[0] == val.__class__.__name__:
                        obj_list.append(str(val))
            if len(line):           
                print(obj_list)
        except NameError:
                print("** class doesn't exist **")
                return


    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"."""
        storage = FileStorage()
        storage.reload()
        line = line.split()
        if len(line) == 0:
            print("** class name missing **")
            return
        elif len(line) == 1:
            print("** instance id missing **")
            return
        elif len(line) == 2:
            print("** attribute name missing **")
            return
        elif len(line) == 3:
            print("** value missing **")
            return
        try:
            eval(line[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = line[0] + "." + line[1]
        obj_dict = storage.all()
        try:
            obj_value = obj_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attr_type = type(getattr(obj_value, line[2]))
            print(type(attr_type))
            line[3] = attr_type(line[3])
            if attr_type == str:
                if line[3][1] == "\"" and line[3][-2] == "\"":
                    line[3] = line[3][0] + line[3][2:-2] + line[3][-1]

            
        except AttributeError:
            pass
        setattr(obj_value, line[2], line[3].replace("\"", "").replace("\'", ""))
        obj_value.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()

