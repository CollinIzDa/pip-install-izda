from collinizda import * # We import everything from the package

def main(): # Lets create a function for showcasing the package

    """
    This is just a function to show the package
    """
    system.clear()
    system.title("This is an example!") # How about to change the console title
    system.write("This is a cool typewriter animation!", .03) # A nice typewriter animation
    say = system.input('Say "Hello World": ', .03, newLine=False) # Also a typewriter animation but as an input
    if say == "Hello World": # We'll see if you put in what I said
        system.write("Hello, how are you?", .03) # If you put in what I said, we'll ask how you're doing
    else: # If you haven't
        system.write("""Noo! I said you have to say "Hello World"!""", .03) # We're telling you to type in "Hello World" like we said above
    system.write("Now press enter 5 times to exit", .03)
    system.enter(5) # Now you have to press enter 5 times to exit
    system._exit(0) # Now we exit so, goodbye!

if __name__ == "__main__":
    main() # We execute the function we created above