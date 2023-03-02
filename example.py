import izda # Import IzDa

def lol(): # Creating our example function
    izda.System.clear() # Clear the command prompt
    izda.System.title("Example") # Changes the title
    izda.System.init() # Allow us to write colors in the command prompt
    izda.System.command("mode 120, 25") # Execute a command
    inputa = izda.Write.Input(f'Write "Hi": ', interval=0.05) # Ask the user to input "Hi"
    if inputa != "Hi": # If he does not input "Hi"
        izda.Write.Print('I said you have to input "Hi"!', interval=0.05) # Say it to him
    else: # If he input "Hi" and did all right
        izda.Write.Print('Like this! Now press enter 5 times to exit.') # Say he have to press enter 5 times to exit
        izda.System.enter(5) # Execute the enter 5 times function

if __name__ == "__main__":
    lol() # Execute our created function on program run
