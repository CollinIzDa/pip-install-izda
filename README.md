![header](https://capsule-render.vercel.app/api?type=waving&color=00ffff&text=CollinIzDa&fontColor=FFF&fontSize=90&animation=fadeIn&fontAlignY=38&desc=pip%20install%20collinizda&descAlignY=51&descAlign=64&height=300&section=header)

<div align="center">
  <img src="https://collinizda.com/img/besen.png"></img>
</div>

<h1 align="center">
  Hello, welcome to the IzDa Repository!
</h1>

<p align="center">
<a href="https://github.com/CollinIzDa/pip-install-collinizda#--installation--">Installation</a> |
<a href="https://github.com/CollinIzDa/IzDa-Bot/blob/main/Changelog.md">Changelogs</a> |
<a href="https://collinizda.com">Website</a>
</p>

> The package "**collinizda**" is just for fun and I coded it because I was bored.
> <br>
> It's not the best packageand my example is shit so don't expect too much

## - Installation -
```ssh
pip3 install collinizda
```

## - Example -
```py
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
        system.write("""Noo! I said you have to say "Hello World"!""") # We're telling you to type in "Hello World" like we said above
    system.write("Now press enter 5 times to exit")
    system.enter() # Now you have to press enter 5 times to exit
    system._exit(0) # Now we exit so, goodbye!

if __name__ == "__main__":
    main() # We execute the function we created above
```

---

🌟 **Enjoyed "collinizda"?** Consider dropping a star :D

**"collinizda" was created by CollinIzDa. 💀**

Discord: CollinIzDa#1594

Website: https://collinizda.com/

![footer](https://capsule-render.vercel.app/api?type=waving&color=00ffff&height=200&section=footer)
