#!/usr/bin/python3
"""
    console module
"""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
        hbnb console class
            Args:
                cmd ([module]): [cmd module for command prompt]
            Returns:
                [bool]: [true or false]
    """
    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel,
               "User": User,
               "State": State,
               "City": City,
               "Amenity": Amenity,
               "Place": Place,
               "Review": Review}
    

    def do_EOF(self, arg):
        """ Exits console """
        return True

    def do_quit(self, arg):
        """ Exits console"""
        return True

    def emptyline(self):
        """ Overwriting empty line method """
        return False

    def do_create(self, args):
        """
             Creates a new instance of BaseModel,
             saves it (to the JSON file) and prints the id
        """

        args = args.split()
        if not args:
            print("** class name missing **")

        elif args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        else:
            b = HBNBCommand.classes[args[0]]()
            b.save()
            print(b.id)

    def do_show(self, args):
        """
            Show command print the dict format of instance
        """

        arg = args.split()
        _all = storage.all()

        if not arg:
            print("** class name missing **")

        elif arg[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        elif len(args.split()) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(args.split()[0], args.split()[1]):
            print("** no instance found **")

        else:
            print(_all["{}.{}".format(args.split()[0], args.split()[1])])

    def do_destroy(self, args):
        """
            Deletes an instance based on the class name and id
        """

        arg = args.split()
        _all = storage.all()

        if not arg:
            print("** class name missing **")

        elif arg[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        elif len(args.split()) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(args.split()[0], args.split()[1]) not in _all:
            print("** no instance found **")

        else:
            del _all["{}.{}".format(args.split()[0], args.split()[1])]
            storage.save()

    def do_all(self, args):
        """
            Prints all string representation of all instances based or
            not on the class name
        """
        args = args.split()
        lst = []
        if args and args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        elif not args:
            for i in storage.all().values():
                lst.append(str(i))
        if len(lst):
            print(lst)

    def do_update(self, args):
        """
            Updates an instance based on the class name and id by
            adding or updating attribute
        """
        _all = storage.all()
        if len(args.split()) == 0:
            print("** class name missing **")

        elif args.split()[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        elif len(args.split()) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(args.split()[0], args.split()[1]) not in _all:
            print("** no instance found **")

        elif len(args.split()) == 2:
            print("** attribute name missing **")

        elif len(args.split()) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args.split()[0], args.split()[1])
            setattr(_all[key], args.split()[2],
                    re.search(r'\w+', args.split()[3]).group())
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
