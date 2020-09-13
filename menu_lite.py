# CircuitPython CLUE menu_lite.py
# Last upated: Aug. 11, 2020, v1.0
# Author(s): James Tobin

#   MIT License
'''
Copyright (c) 2020 James Tobin
Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to the following
conditions:
The above copyright notice and this permission notice shall be included in all copies
or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.
'''

#   Version Notes
'''
v1.0
    - Creats list of available files and displays them on CLUE's display
    - Press and hold the A button at the beginning to ender small text mode (default: large text mode)
    - Press and hold A and B to see terminal
    - Press A to select next file (loops at end)
    - Press B to run the selected file

    Note:
        - File names that start with '.', '_', and 'TRASH' are automatiically filtered out.
        - These full file names are also filtered out: 
            -'boot_out.txt', 'main.py', 'code.py', 'menu.py', 'main.txt', 'code.txt'
'''

import time
import os

from adafruit_clue import clue 
#Cutebot users uncomment lines below and comment out line above
#from jisforjt_cutebot_clue import cutebot, clue                  

arrow = '->'
selected = 0
move_count = 0
hidden_ID = ['.', '_', 'TRASH', 'boot_out.txt', 'main.py', 'code.py', 'menu.py', 'main.txt', 'code.txt']         # List of file name elements and names we do not want to see
start_pos = 0

def file_filter(data):
    for y in hidden_ID:
        filtered_data = [x for x in data if not x.startswith(y)]
        data = filtered_data
    filtered_data = [x for x in data if x[-3:] == '.py' or x[-4:] == '.txt' ]
    return sorted(filtered_data)

print("\nPRESS AND HOLD A BUTTON TO ENTER SMALL TEXT MODE\n.")
time.sleep(2)
if clue.button_a:
    small_text_mode = True
    print('Starting small text mode.')
else:
    small_text_mode = False
    print('NO PRESS DETECTED.\nStarting large text mode.')
menu_options = file_filter(os.listdir())
max_length = len(menu_options)
if small_text_mode == True:
    clue_data = clue.simple_text_display(title="Menu", title_scale=2, text_scale=1)
    maxLineLen = min(max_length, 15)
else:
    clue_data = clue.simple_text_display(title="Menu", title_scale=3, text_scale=2)
    maxLineLen = min(max_length, 6)

while True:
    indicator = ['  '] * max_length
    indicator[selected] = arrow
    j = start_pos
    for i in range(0, maxLineLen, 1):
        clue_data[i].text = "{} {}".format(indicator[j], menu_options[j])
        j += 1
    clue_data[maxLineLen].text = "File {} of {}".format((selected + 1), max_length)
    clue_data.show()
    if clue.button_a and clue.button_b:
        clue_data.show_terminal()
        time.sleep(0.1)
    elif clue.button_a:
        move_count += 1
        selected = move_count % max_length
        if selected > (start_pos + maxLineLen - 1):
            start_pos += 1
        elif selected < start_pos:
            start_pos = 0
        time.sleep(0.1)
    elif clue.button_b:
        clue_data.show_terminal()
        exec(open(menu_options[selected]).read())
        time.sleep(2)
