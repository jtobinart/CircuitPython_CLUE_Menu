
# CircuitPython_CLUE_Menu
[![CircuitPython_CLUE_Menu YouTube Video](https://github.com/jisforjt/CircuitPython_CLUE_Menu/blob/master/docs/images/youtubestill.png)](https://youtu.be/ZTE-hqM6GPo)

Make your Adafruit [CLUE](https://www.adafruit.com/product/4500) multi-functional by adding a nifty startup menu to select the program you want to run. You no longer need to rename your files to code or main to run them. Simply drag and drop your files into your CIRCUITPY drive and this menu program does the rest.

## Dependencies
This library depends on:
* [Adafruit CircuitPython](https://github.com/adafruit/circuitpython)
* [Adafruit_CircuitPython_CLUE](https://github.com/adafruit/Adafruit_CircuitPython_CLUE) or [CircuitPython_CLUE_Cutebot](https://github.com/jisforjt/CircuitPython_CLUE_Cutebot)

## Instalations
Follow Adafruit's [CLUE Overview](https://learn.adafruit.com/adafruit-clue) instructions under _CircuitPython on CLUE_. During the installation process, you will download the latest _library bundle_ and transfer several libraries to the CLUE, including the _Adafruit_CircuitPython_CLUE_. If you are using this with the ElecFreak's micro:bit Smart [Cutebot](https://www.elecfreaks.com/micro-bit-smart-cutebot.html) then follow the installation directions provided in the [CircuitPython_CLUE_Cutebot](https://github.com/jisforjt/CircuitPython_CLUE_Cutebot) repository.

Download this repository and copy _main.py_ and at least one of the following files over to your CIRCUITPY drive.
file | description
---- | ----
menu.py | Original Python file and is highly detailed
menu.mpy | Precompiled Python file and a third the size of _menu.py_
menu_lite.py | Editable Python file and less than half the size of _menu.py_
menu_cubot.mpy |Precompiled Python file for use with [CircuitPython_CLUE_Cutebot](https://github.com/jisforjt/CircuitPython_CLUE_Cutebot) repository

## Configuration
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
