# CircuitPython_CLUE_Menu
Make your Adafruit [CLUE](https://www.adafruit.com/product/4500) multi-functional by adding a nifty startup menu to select the program you want to run. You no longer need to rename you files to main.py

## Dependencies
This library depends on:
* [Adafruit CircuitPython](https://github.com/adafruit/circuitpython)
* [Adafruit_CircuitPython_CLUE](https://github.com/adafruit/Adafruit_CircuitPython_CLUE)

## Instalations
Follow Adafruit's [CLUE Overview](https://learn.adafruit.com/adafruit-clue) instructions under _CircuitPython on CLUE_. During the installation process, you will download the latest _library bundle_ and transfer several libraries to the CLUE, including the __Adafruit_CircuitPython_CLUE__.
Download this repository and copy _main.py_ and _menu.py_ over to your drive CIRCUITPY. 

## On Startup
The scripts will automatically run at startup. You don't need to do anything else after installation.

If you wish to disable the menu and run another file at startup, I suggest modifying _main.py_. _Main.py_ is a simple redirect script and is a lot easier than constantly renaming files.

Save time by changing the imported file in __Main.py__. It is set up by default to run menu.py
```python
import menu
```
If you wanted to run another program at startup, for example hello_world.txt, it would be:
```python
#import menu
import hello_world
```
It is that easy. I only change __Main.py__ when I am debugging a new program.

## Usage
This menu program has two display modes: small text and large text mode. The program will automatically start in large test mode. During boot up of the menu program you will be given a chance to press the A button to switch to small text mode.

Once the menu opens you can press:
Button | Action
------ | ------
A | Select next file
B | Run selected file
A and B | Show terminal, while pressed

## License
The code of the repository is made available under the terms of the MIT license. See license.md for more information.
