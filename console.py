#!/usr/bin/python3
"""This program contains the entry point of the command interpreter."""


import cmd
import json


class HBNBCCommand(cmd.Cmd):
    """Class for the command interpreter"""

    prompt = "(hbnb)"

    def do_EOF(self, arg):
        """Handles End of File character."""
        pass

    def do_quit(self, arg):
        """Exits the program."""
        pass
    
    def do_create(self, arg):
        """Creates an instance."""
        pass

    def do_show(self, arg):
        """Prints the string representtation of an instance."""
        pass

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        pass

    def do_all(self, arg):
        """Prints all string representation of all instance."""
        pass

    def do_update(self, arg):


if __name__ == '__main__':
    HBNBCommand().cmdloop()
