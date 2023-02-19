# ================================ #
#        CollinIzDa Package        #
#      https://collinizda.com      #
# ================================ #

# Copyright (c) CollinIzDa#1594
# That package was proudly coded by CollinIzDa#1594
# Its not done yet. If there any bugs, contact me: CollinIzDa#1594 or info@collinizda.de

#~~~ Imports ~~~#
from pystyle import Cursor
from time import sleep as _sleep
from sys import stdout as _stdout
from ctypes import windll as _windll
from typing import NoReturn, TypeAlias
from os import name as _name, system as _system
#~~~ Imports ~~~#


#~~~ Variables ~~~#
__version__ = "1.0.2"
#~~~ Variables End ~~~#


#~~~ All functions ~~~#
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
"""

Windows = _name == "nt"
Linux = _name == "posix"
_ExitCode: TypeAlias = str | int | None

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
    
    else: # What os are you using???
        pass # I do nothing


def init(): # Make colors printable into the console
    _system("")

def _exit(__status: _ExitCode = None) -> NoReturn: ...

def enter(times: str): # Press enter 5 times to exit
    [input(i) for i in range(times, 0, -1)]  # Wait for 5 enter presses

def command(command: str): # Execute a terminal command
    return _system(command) # _system is os.system("the command e.g cls")

class write():
    def print(text: str, speed: float, newLine=True): # A fancy typewriter input function
        Cursor.HideCursor()
        for i in text:  # Loop over the message
            # Print the one charecter, flush is used to force python to print the char
            print(i, end="", flush=True)
            _sleep(speed)  # Sleep a little before the next one
        if newLine:  # Check if the newLine argument is set to True
            print()  # Print a final newline to make it act more like a normal print statement
        Cursor.ShowCursor()

    def input(text: str, speed: float, newLine=True): # A fancy typewriter input function
        Cursor.HideCursor()
        for i in text:  # Loop over the message
            # Print the one charecter, flush is used to force python to print the char
            print(i, end="", flush=True)
            _sleep(speed)  # Sleep a little before the next one
        if newLine:  # Check if the newLine argument is set to True
            print()  # Print a final newline to make it act more like a normal print statement
        Cursor.ShowCursor()
        return input()
#~~~ All functions End ~~~#
