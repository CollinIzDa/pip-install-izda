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

from time import sleep as _sleep
from pystyle import Cursor
#~~~ Imports ~~~#

"""
0 variables:
    Nothing here...

2 functions:
    print()    |    prints any text with a nice typewriter animation
    input()    |    writes an input text with a nice typewriter animation
"""

def Print(text: str, interval=0.05, show_cursor=True, newLine=False): # A fancy typewriter input function
    Cursor.HideCursor() # Hides the cursor for a better animation
    for i in text:  # Loop over the message
        # Print the one charecter, flush is used to force python to print the char
        print(i, end="", flush=True)
        _sleep(interval)  # Sleep a little before the next one
    if newLine:  # Check if the newLine argument is set to True
        print()  # Print a final newline to make it act more like a normal print statement
    if show_cursor:
        Cursor.ShowCursor() # Shows the cursor again

def Input(text: str, interval=0.05, show_cursor=True, newLine=False): # A fancy typewriter input function
    Cursor.HideCursor() # Hides the cursor for a better animation
    for i in text:  # Loop over the message
        # Print the one charecter, flush is used to force python to print the char
        print(i, end="", flush=True)
        _sleep(interval)  # Sleep a little before the next one
    if newLine:  # Check if the newLine argument is set to True
        print()  # Print a final newline to make it act more like a normal print statement
    if show_cursor:
        Cursor.ShowCursor() # Shows the cursor again
    return input() # returns input that we can input things in this text