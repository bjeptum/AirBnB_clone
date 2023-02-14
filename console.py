#!/usr/bin/python3
"""This program contains the entry point of the command interpreter."""


import cmd
from models.base_model import BaseModel
import models
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter"""

    prompt = "(hbnb)"
    class_names = [
            BaseModel,
            User,
            State,
            City,
            Amenity,
            Place,
            Review
            ]

    def do_EOF(self, arg):
        """Handles End of File character."""
        print()
        return True

    def do_quit(self, arg):
        """Quit command that Exits the program."""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates an instance."""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_ = eval(arg)
            if issubclass(class_, BaseModel):
                new_instance = class_()
                storage.new(new_instance)
                storage.save()
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
                key = "{}.{}".format(args[0], args[1])
                if key in storage.all().keys():
                    print(storage.all()[key])
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
            if issubclass(class_, BaseModel):
                key = "{}.{}".format(args[0], args[1])
                if key in storage.all().keys():
                    del storage.all()[key]
                    storage.save()
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
                key = "{}.{}".format(args[0], args[1])
                if key in storage.all().keys():
                    if len(args) < 3:
                        print("** attribute name missing **")
                        return
                    if len(args) < 4:
                        print("** value missing **")
                        return
                    if args[2] in ["id", "created_at", "updated_at"]:
                        print("** can't update id, created_at, updated_at **")
                        return
                    try:
                        value = eval(args[3])
                        value = args[3].strip("\"")
                        setattr(storage.all()[key], args[2], value)
                        storage.all()[key].save()
                    except (NameError, SyntaxError):
                        raise (NameError, SyntaxError)
                else:
                    print("** no instance found **")
            else:
                raise NameError
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
