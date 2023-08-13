**AirBnB_clone**

AirBnB Clone Project :

Embarking upon the AirBnB Clone venture! The primary ambition of this undertaking resides in the construction of a distilled rendition of the AirBnB platform. Central to our focus is the formulation of a command-line-driven entity administration framework. This comprehensive README furnishes a panoramic survey of the enterprise, the command interpreter, initiation protocols, operational guidelines, as well as illustrative instances of utilization.

# Project Overview :

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.



# Command Interpreter :

The command interpreter serves as a conduit, facilitating your engagement with the AirBnB framework via the terminal interface. It affords you the capacity to effectuate a spectrum of operations, encompassing the creation, retrieval, modification, and removal of entities. This segment expounds upon the initiation protocol of the interpreter, its operational nuances, and proffers instances of illustrative commands.

# Starting the Interpreter:

1.Clone or download this project to your computer.

```https://github.com/younis-alx/AirBnB_clone.git```

2.Open your terminal and navigate to the project's main directory.

`cd AirBnB_clone`

3.Run the following command:

`python3 console.py`


# Using the Interpreter:

|Command|Example|Functionality| Return
|----|-------------------------------|-----------------------------|------------|
|create|`'create [class]'`            |Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the `id`. Ex: `$ create BaseModel`| uuid            |
|show|`'show [class] [uuid]'`            |      Prints the string representation of an instance based on the class name and `id`      |all dictionary with all stored info on uuid
|update|`update BaseModel [uuid] [key] [value]`|Updates an instance based on the class name and `id` by adding or updating attribute |None
|destroy|`destroy [class][uuid]`|Deletes an instance based on the class name and `id` |None
|all|`all [class]`|Prints all string representation of all instances based or not on the class name|all dictionary with of object


