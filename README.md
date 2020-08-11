# CircuitPython_CLUE_Menu
Make your AAdafruit [CLUE](https://www.adafruit.com/product/4500) multifunctional by adding a nifty startup menu to select the program you want to run. You no longer need to retitle you files to main.py

## Dependencies
This library depends on:
* [Adafruit CircuitPython](https://github.com/adafruit/circuitpython)
* [Adafruit_CircuitPython_CLUE](https://github.com/adafruit/Adafruit_CircuitPython_CLUE)

## Instalations
Follow Adafruit's [CLUE Overview](https://learn.adafruit.com/adafruit-clue) instructions under _CircuitPython on CLUE_. During the installation process, you will download the latest _library bundle_ and transfer several libraries to the CLUE, including the __Adafruit_CircuitPython_CLUE__.
Download this repository and copy _main.py_ and _menu.py_ over to your drive CIRCUITPY. 

## Usage
You can create a new main.py file and use:
```python
import cutebot
from cutebot import clue
```
to access the CLUE and Cutebot or you can use one of the examples programs provided in the repository. Use the IR remote example to easily learn about IR signals and control your Cutebot in a snap. Download Adafruit's BlueFruit Connect app and control your Cutbot over Bluetooth. These examples and more are located in the _examples_ folder.

## License
The code of the repository is made available under the terms of the MIT license. See license.md for more information.
