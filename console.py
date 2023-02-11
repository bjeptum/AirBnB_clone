#!/usr/bin/python3
"""This program contains the entry point of the command interpreter."""


import cmd
import json


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter"""

    prompt = "(hbnb)"

    def do_EOF(self, arg):
        """Handles End of File character."""
        print()
        return True

    def do_quit(self, arg):
        """Quit command that Exits the program."""
        return True

    def do_create(self, line):
        """Creates an instance."""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesnt't exist **")
        else:
            """
            If the line is in the storage class() method,
            create an instance
            of the line and print the id
            """
            new_instance = storage.classes()[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representtation of an instance."""
        """
        if line == "" or line is None:
            print("** class name missing **")
            return
        line = line.split()
        if len(line) == 1:
            print("** instance id missing **")
            return
        class_name = line[0]
        class_id = line[1]
        if class_name not in model.storage.all():
            print("** class doesn't exist **")
            return
        instances = models.storage.all()[class_name]
        if class_id not in instances:
            print("** no instance found **")
            return
        print(instances[class_id]
        """

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        pass

    def do_all(self, arg):
        """Prints all string representation of all instance."""
        pass

    def do_update(self, arg):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
