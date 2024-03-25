#!/usr/bin/env python3

import cmd
import sys

class Command(cmd.Cmd):
    """This is a simple command line interpreter"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exits the console with EOF"""
        print()
        return True
    
    def do_quit(self, line):
        """Exit the console with 'quit'"""
        sys.exit(0)

if __name__ == "__main__":
    Command().cmdloop()
    
