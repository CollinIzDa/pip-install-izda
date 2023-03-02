![header](https://capsule-render.vercel.app/api?type=waving&color=00ffff&text=CollinIzDa&fontColor=FFF&fontSize=90&animation=fadeIn&fontAlignY=38&desc=pip%20install%20izda&descAlignY=51&descAlign=67&height=300&section=header)

<div align="center">
  <img src="https://collinizda.com/img/besen.png"></img>
</div>

<h1 align="center">
  Hello, welcome to the "izda" Repository!
</h1>

<p align="center">
<img alt="Version" src="https://img.shields.io/badge/version-1.0.3-blue.svg?cacheSeconds=2592000" />
<a href="https://pepy.tech/project/collinizda" target="_blank">
<img alt="Downloads" src="https://static.pepy.tech/personalized-badge/collinizda?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads" /></a>
<img src="https://img.shields.io/github/languages/top/CollinIzDa/pip-install-collinizda?style=flat-square" </a>
<img src="https://img.shields.io/github/license/CollinIzDa/pip-install-collinizda?style=flat-square" </a>
</p>

<p align="center">
<a href="https://github.com/CollinIzDa/pip-install-collinizda#---installation--">Installation</a> |
<a href="https://github.com/CollinIzDa/pip-install-collinizda/blob/main/Changelog.md">Changelogs</a> |
<a href="https://collinizda.com">Website</a>
</p>

> The package "**izda**" is just for fun and I coded it because I was bored.
> <br>
> It's not the best packageand my example is shit so don't expect too much

## - 📥 Installation -
```ssh
pip3 install izda
```

## - Functions in dropdown -
<details>
<summary>All functions with examples (Drop Down)</summary>

## - ❗ Title Function -
```py
import izda # Import the libary

izda.System.title("This is the Title!") # Change the title
```

## - Clear Function -
```py
Import izda # Import the libary

izda.System.clear() # Clears the console
```

## - Write and Input -
```py
import izda # Import the libary

izda.Write.Print("Typewriter function", interval=0.05) # Typewriter print function
izda.Write.Print("Typewriter input function", interval=0.05, newLine=False) # Typewriter input animation
# The "interval" in the function is the speed and the "newLine=..." is to print a new line after the animation
# You can also use cursor=False/True if you want to show the command prompt cursor or not
```

## - All other -
```py
import izda # Import the libary

izda.System.init() # Allows you to use colors in print
izda.System.command("echo Hello") # Execute a command into the console
izda.System.enter(5) # Press enter 5 times to exit
```
</details>

---

## - 👤 Authors -
👤 Github: [@**CollinIzDa**](https://github.com/collinizda)<br>
👤 Website: [**CollinIzDa.com**](https://collinizda.com/)

## - 📍 Example -
```py
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
```

---

🌟 **Enjoyed "izda"?** Consider dropping a star :D

**"izda" was created by CollinIzDa.**

Discord: CollinIzDa#1594

Website: https://collinizda.com/

![footer](https://capsule-render.vercel.app/api?type=waving&color=00ffff&height=200&section=footer)
