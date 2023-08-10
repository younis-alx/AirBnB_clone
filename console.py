#!/usr/bin/python3

import cmd
from models.base_model import BaseModel

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


    def do_show(self, line):
         """Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234."""
        
         
if __name__ == '__main__':
        HBNBCommand().cmdloop()

