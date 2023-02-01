#!/usr/bin/python3
"""
    console module
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
        hbnb console class
    	    Args:
                cmd ([module]): [cmd module for command prompt]
            Returns:
                [bool]: [true or false]
    """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """ Exits console """
        return True
    def do_quit(self, arg):
        """ Exits console	"""
        return True
    def emptyline(self):
        """ Overwriting empty line method """
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
