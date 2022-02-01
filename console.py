#!/usr/bin/python3
"""
Console.py is a program that contains the entry point of the\
 command interpreter
"""


import cmd
import models
import shlex
import sys


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand class: a custom command line interperter"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Implementing quit to exit the program"""
        return True

    def do_EOF(self, arg):
        """Implementing EOF to exit the program"""
        return True

    def emptyline(self):
        """shouldn’t execute anything when no command is passed to exercute"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
