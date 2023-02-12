#!/usr/bin/python3
"""This program contains the entry point of the command interpreter."""


import cmd
from models.base_model import BaseModel
import models
from models.engine.file_storage import FileStorage
import json


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter"""

    prompt = "(hbnb)"
    storage = FileStorage()

    def do_EOF(self, arg):
        """Handles End of File character."""
        print()
        return True

    def do_quit(self, arg):
        """Quit command that Exits the program."""
        return True

    def do_create(self, arg):
        """Creates an instance."""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_ = eval(arg)
            if issubclass(class_, BaseModel):
                new_instance = class_()
                HBNBCommand.storage.new(new_instance)
                HBNBCommand.storage.save()
                print(new_instance.id)
            else:
                raise NameError
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representtation of an instance."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            class_ = eval(args[0])
            if issubclass(class_, BaseModel):
                key = "{}.{}".format(args[0]. args[1])
                if key in HBNCommand.storage.all().keys():
                    print(HBNCommand.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                raise NameError
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            class_ = eval(args[0])
            if issubclass(class_. BaseModel):
                key = "{}.{}".format(args[0], args[1])
                if key in HBNBCommand.storage.all().keys():
                    del HBNBCommand.storage.all()[key]
                    HBNBCommand.storage.save()
                else:
                    print("** no instance found **")
            else:
                raise NameError
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if arg:
            if arg not in globals():
                print("** class doesn't exist **")
            else:
                instances = [str(instance) for instance
                             in storage.all().values()
                             if type(instance).__name__ == arg]
                print(instances)
        else:
            print([str(instance) for instance in storage.all().values()])

    def do_update(self, arg):
        """Adds and updates attribute to an instance"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
