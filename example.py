import collinizda # How about importing collinizda?

def main(): # Lets create a function for showcasing the package

    """
    This is just a function to show the package
    """
    collinizda.clear()
    collinizda.title("This is an example!") # How about to change the console title
    collinizda.write.print("This is a cool typewriter animation!", .03) # A nice typewriter animation
    say = collinizda.write.input('Say "Hello World": ', .03, newLine=False) # Also a typewriter animation but as an input
    if say == "Hello World": # We'll see if you put in what I said
        collinizda.write.print("Hello, how are you?", .03) # If you put in what I said, we'll ask how you're doing
    else: # If you haven't
        collinizda.write.print("""Noo! I said you have to say "Hello World"!""", .03) # We're telling you to type in "Hello World" like we said above
    collinizda.write.print("Now press enter 5 times to exit", .03)
    collinizda.enter(5) # Now you have to press enter 5 times to exit
    collinizda._exit(0) # Now we exit so, goodbye!

if __name__ == "__main__":
    main() # We execute the function we created above
