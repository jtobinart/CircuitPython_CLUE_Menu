# CircuitPython_CLUE_Menu
Make your Adafruit [CLUE](https://www.adafruit.com/product/4500) multi-functional by adding a nifty startup menu to select the program you want to run. You no longer need to rename you files to code.py, code.txt, main.py, or main.txt to run them.

## Dependencies
This library depends on:
* [Adafruit CircuitPython](https://github.com/adafruit/circuitpython)
* [Adafruit_CircuitPython_CLUE](https://github.com/adafruit/Adafruit_CircuitPython_CLUE)

## Instalations
Follow Adafruit's [CLUE Overview](https://learn.adafruit.com/adafruit-clue) instructions under _CircuitPython on CLUE_. During the installation process, you will download the latest _library bundle_ and transfer several libraries to the CLUE, including the _Adafruit_CircuitPython_CLUE_.

Download this repository and copy _main.py_ and at least one of the following files over to your CIRCUITPY drive.
file | description
---- | ----
menu.py | Original Python file and is highly detailed
menu.mpy | Precompiled Python file and a third the size of _menu.py_
menu_lite.py | Editable Python file and less than half the size of _menu.py_
menu_cubot.mpy |Precompiled Python file for use with [CLUE-Cutebot-CircuitPython](https://github.com/jisforjt/CLUE-Cutebot-CircuitPython) repository

## On Startup
If you are not using _menu.py_ or _menu.mpy_ then you will need to edit _main.py_. _main.py_ is a simple redirect script and it is a lot easier than constantly renaming files. Open _main.py_ and you will see:
```python
#Uncomment the version you are using and comment out the rest.
import menu
#import menu_lite
#import menu_cutebot
```
If you are using menu_lite then change it to:
```python
#Uncomment the version you are using and comment out the rest.
#import menu
import menu_lite
#import menu_cutebot
```
If you wanted to run another program at startup, for example hello_world.txt, it would be:
```python
#import menu
#import menu_lite
#import menu_cutebot
import hello_world
```
It is that easy. I only change __main.py__ when I am debugging a new program.

## Usage
This menu program has two display modes: small and large text modes. The program will automatically start in large text mode. During boot up of the menu program you will be given a chance to press the A button to switch to small text mode.

Once the menu opens you can press:
Button | Action
------ | ------
A | Select next file
B | Run selected file
A and B | Show terminal, while pressed

## License
The code of the repository is made available under the terms of the MIT license. See license.md for more information.
