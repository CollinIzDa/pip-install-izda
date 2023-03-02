# ================================== #
#        CollinIzDa's Library        #
#       https://collinizda.com       #
# ================================== #

# Copyright (c) CollinIzDa#1594
# That package was proudly coded by CollinIzDa#1594
# Its not done yet. If there any bugs or problems,
# create an issue on my github https://github.com/CollinIzDa/pip-install-collinizda/issues/new

#~~~ Imports ~~~#
import sys
sys.dont_write_bytecode = True

from sys import stdout as _stdout
from ctypes import windll as _windll
from os import name as _name, system as _system
#~~~ Imports ~~~#

"""
3 variables:
    Windows    |    checks if the user is on the windows os or not
    Linux      |    checks if the user is on the linux os or not
    _ExitCode  |    Exit code for the _exit function

5 functions:
    clear()    |    clears the terminal
    title()    |    changes the console title
    write()    |    prints out words a little more fancier
    init()     |    initialize the terminal to allow the use of colors
    exit()     |    exits the terminal
    command()  |    execute a command into the console

NOTE: Bugs are possible because the library is not finished yet.
"""

Windows = _name == "nt"
Linux = _name == "posix"

def clear():
    if Windows:
        # If the os is windows
        _system("cls")
    elif Linux:
        # If the os is linux
        _system("clear")
    else:
        # I don't know what you are using
        print("\n"*120)

def title(_str):
    if Windows: # Checks if the user is using windows
        _windll.kernel32.SetConsoleTitleW(f"{_str}") # Update the title of the command promt

    elif Linux:
        _stdout.write(f"\x1b]0;{_str}\x07") # Update the title of the command promt
    
    else: # Bro what os are you using???
        pass # I do nothing

def init(): # initialize the terminal to allow the use of colors
    _system("")

def enter(times: str): # Press enter 5 times to exit
    return [input(i) for i in range(times, 0, -1)]  # Wait for 5 enter presses

def command(command: str): # Execute a terminal command
    return _system(command) # _system is os.system("the command e.g cls")