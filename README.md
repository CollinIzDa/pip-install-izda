![header](https://capsule-render.vercel.app/api?type=waving&color=00ffff&text=CollinIzDa&fontColor=FFF&fontSize=90&animation=fadeIn&fontAlignY=38&desc=pip%20install%20collinizda&descAlignY=51&descAlign=64&height=300&section=header)

<div align="center">
  <img src="https://collinizda.com/img/besen.png"></img>
</div>

<h1 align="center">
  Hello, welcome to the IzDa Repository!
</h1>

<p align="center">
<a href="https://github.com/CollinIzDa/pip-install-collinizda#---installation--">Installation</a> |
<a href="https://github.com/CollinIzDa/pip-install-collinizda/blob/main/Changelog.md">Changelogs</a> |
<a href="https://collinizda.com">Website</a>
</p>

> The package "**collinizda**" is just for fun and I coded it because I was bored.
> <br>
> It's not the best packageand my example is shit so don't expect too much

## - 📥 Installation -
```ssh
pip3 install collinizda
```

## - Functions in dropdown -
<details>
<summary>All functions with examples (Drop Down)</summary>

## - ❗ Title Function -
```py
import collinizda # Import the libary

collinizda.title("This is the Title!") # Change the title
```

## - Clear Function -
```py
Import collinizda # Import the libary

collinizda.clear() # Clears the console
```

## - Write and Input -
```py
import collinizda # Import the libary

collinizda.write.print("Typewriter function", .03) # Typewriter print function
collinizda.write.input("Typewriter input function", .03, newLine=False) # Typewriter input animation
# The ", .03" in the function is the speed and the "newLine=..." is to print a new line after the animation
```

## - All other -
```py
import collinizda # Import the libary

collinizda.init() # Allows you to use colors in print
collinizda.command("echo Hello") # Execute a command into the console
collinizda.enter(5) # Press enter 5 times to exit
collinizda._exit(0) # Exit the programm with the exit code 0
```
</details>

---

## - 👤 Authors -
👤 Github: [@**CollinIzDa**](https://github.com/collinizda)<br>
👤 Website: [**CollinIzDa.com**](https://collinizda.com/)

## - 📍 Example -
```py
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
```

---

🌟 **Enjoyed "collinizda"?** Consider dropping a star :D

**"collinizda" was created by CollinIzDa. 💀**

Discord: CollinIzDa#1594

Website: https://collinizda.com/

![footer](https://capsule-render.vercel.app/api?type=waving&color=00ffff&height=200&section=footer)
