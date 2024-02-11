#!/usr/bin/python3
"""This module is the console and is entry point of the command interpreter"""

import cmd
import json
import re
import sys
from shlex import split
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def parse(argv: str) -> list:
    """
    Splits the argv string based a specified pattern

    :param argv: string
    :return:  A list of words from the parsed string
    """
    curly_brackets = re.search(r"\{(.*?)\}", argv)
    brackets = re.search(r"\[(.*?)\]", argv)
    if not curly_brackets:
        if not brackets:
            return [i.strip(",") for i in split(argv)]
        else:
            temp = split(argv[:brackets.span()[0]])
            result = [i.strip(",") for i in temp]
            result.append(brackets.group())
            return result
    else:
        temp = split(argv[:curly_brackets.span()[0]])
        result = [i.strip(",") for i in temp]
        result.append(curly_brackets.group())
        return result


def validate(args):
    """
    Validate the args
    Args:
        args: String containing the command arguments.
    Returns:
        The arguments if they exist and are valid. Else, an error message.
    """
    arguments = parse(args)
    if len(arguments) == 0:
        print("** class name missing **")
    elif arguments[0] not in HBNBCommand.classes:
        print("** class doesn't exist **")
    else:
        return arguments


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter for the AirBnB clone"""

    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def emptyLine(self):
        """Handles the behaviour when an empty line is entered"""
        pass

    def default(self, args):
        """Handles default behavior for cmd module when input is invalid"""
        commands = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }

        match_found = re.search(r"\.", args)
        if match_found is not None:
            arg = [args[:match_found.span()[0]], args[match_found.span()[1]:]]
            match_found = re.search(r"\((.*?)\)", arg[1])
            if match_found is not None:
                new_cmd = [arg[1][:match_found.span()[0]],
                           match_found.group()[1:-1]]
                if new_cmd[0] in commands.keys():
                    execute = f"{arg[0]} {new_cmd[1]}"
                    return commands[new_cmd[0]](execute)
        print("*** Unknown syntax: {}".format(args))
        return False

    def do_count(self, args):
        """Returns the number of instances of a class"""
        arg_list = parse(args)
        count = 0
        for obj in storage.all().values():
            if arg_list[0] == type(obj).__name__:
                count += 1
        print(count)

    def do_quit(self, args):
        """Handles the command to exit the program"""
        return True

    def do_EOF(self, args):
        """Handles the EOF command to exit the program"""
        print()
        return True

    def do_create(self, args):
        """
        Creates an instance of a class and returns its id.
        [USAGE]: create <class>
        """
        arg_list = validate(args)
        if arg_list:
            print(eval(arg_list[0])().id)
            storage.save()

    def do_show(self, args):
        """
        Prints the string representation of a class instance
        based on its name and id.
        [USAGE]: show <class> <id>
        """
        arg_list = validate(args)
        if arg_list:
            if len(arg_list) != 2:
                print("** instance id missing **")
            else:
                key = f"{arg_list[0]}.{arg_list[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, args):
        """
        Deletes a class instance based on its name and id
        [USAGE]: destroy <class> <id>
        """
        arg_list = validate(args)
        if arg_list:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(*arg_list)
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, args):
        """
        Prints a string representation of all instances
        [USAGE]: all <class> or <class>.all()
        """
        arg_list = split(args)
        obj = storage.all().values()
        if not arg_list:
            print([str(item) for item in obj])
        else:
            if arg_list[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                print([str(item) for item in obj if arg_list[0] in str(item)])

    def do_update(self, args):
        """
        Updates a class instance based on its name and id by adding to or
        updating its attributes
        [USAGE]: update <class> <id> <name> "<value>"
        """
        arg_list = validate(args)
        if arg_list:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                print("arglistt is more than 1")
                curr_id = f"{arg_list[0]}.{arg_list[1]}"
                if curr_id in storage.all():
                    if len(arg_list) == 2:
                        print("** attribute name missing **")
                    elif len(arg_list) == 3:
                        if type(eval(arg_list[2])) == dict:
                            obj = storage.all()["{}.{}".format(arg_list[0],
                                                               arg_list[1])]
                            for k, v in eval(arg_list[2]).items():
                                if (k in obj.__class__.__dict__.keys() and
                                        type(obj.__class__.__dict__[k])
                                        in {str, int, float}):
                                    valtype = type(obj.__class__.__dict__[k])
                                    obj.__dict__[k] = valtype(v)
                                else:
                                    obj.__dict__[k] = v
                        else:
                            print("** value missing **")
                    else:
                        tmp = storage.all()[curr_id]
                        if arg_list[2] in type(tmp).__dict__:
                            rt_type = type(tmp.__class__.__dict__[arg_list[2]])
                            setattr(tmp, arg_list[2], rt_type(arg_list[3]))
                        else:
                            setattr(tmp, arg_list[2], arg_list[3])
                else:
                    print("** no instance found **")
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
