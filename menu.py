# CircuitPython CLUE menu.py
# Last upated: Aug. 11, 2020, v1.0
# Author(s): James Tobin

######################################################
#   MIT License
######################################################
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

######################################################
#   Version Notes
######################################################
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


######################################################
#   Import
######################################################
import time
import os                                       
from adafruit_clue import clue                  

#import cutebot                                 # if you were using this with the CLUE and Cutebot
#from cutebot import clue


######################################################
#   Global Variables
######################################################
arrow = '->'                                    # Graphic for display
selected = 0                                    # The index of the currently selected file
move_count = 0                                  # The number of times we have moved
hidden_ID = ['.', '_', 'TRASH', 'boot_out.txt', 'main.py', 'code.py', 'menu.py', 'main.txt', 'code.txt']         # List of file name elements and names we do not want to see
start_pos = 0                                   # Starting position for the simple_text_display list


######################################################
#   Functions
######################################################
'''
file_filter(data) - Filters out the files we don't want to see
    - data: a list of files

Countdown(duration) - Simple countdown clock
    - duration: the number of seconds you want the countdown to last. The minimum duration is 1 second.
'''

def file_filter(data):
    for y in hidden_ID:
        filtered_data = [x for x in data if not x.startswith(y)]                   # Hide files that start with items in our hidden_ID list
        data = filtered_data
    filtered_data = [x for x in data if x[-3:] == '.py' or x[-4:] == '.txt' ]      # Show only files that end with '.py' or '.txt'
    return sorted(filtered_data)                                                   # Return an alphabetically sorted list

def countdown(duration):
    duration = max(duration, 1)                         # Check and set duration to at least 1 second
    duration/=4                                         # Set duration to a quarter of itself
    clue_data[0].text = '3'                             # Set countdown status
    clue_data.show()                                    # Display countdown status
    clue.play_tone(1046.5,duration)                     # Play tone
    clue_data[0].text = '2'
    clue_data.show()
    clue.play_tone(1147.7,duration)
    clue_data[0].text = '1'
    clue_data.show()
    clue.play_tone(1568,(duration*2))


######################################################
#   Main Code
######################################################
print("\nPRESS AND HOLD A BUTTON AT STARTUP TO ENTER SMALL TEXT MODE\n.")
time.sleep(2)                                           # Give the user a chance to press the button
if clue.button_a:
    small_text_mode = True
    print('Starting small text mode.')
else:
    small_text_mode = False
    print('NO PRESS DETECTED.\nStarting large text mode.')

menu_options = file_filter(os.listdir())                # Set menu options
max_length = len(menu_options)
#indicator = ['  '] * max_length                  # Create a list with three empty spaces, sames size as menu_options
#indicator[0] = arrow                             # Set the arrow graphic starting position

if small_text_mode == True:
    # small text mode settings
    clue_data = clue.simple_text_display(title="Menu", title_scale=2, text_scale=1)     # Create a simple_text_display
    maxLineLen = min(max_length, 15)                                                    # Set number of available text lines on the display to whichever is smaller
else:
    # large text mode settings
    clue_data = clue.simple_text_display(title="Menu", title_scale=3, text_scale=2)     # Create a simple_text_display
    maxLineLen = min(max_length, 6)                                                     # Set number of available text lines on the display to whichever is smaller


######################################################
#   Main Loop
######################################################
while True:
    indicator = ['  '] * max_length     # Create a list with three empty spaces, sames size as menu_options
    indicator[selected] = arrow         # Set the arrow graphic position
    
    # Display text
    j = start_pos
    for i in range(0, maxLineLen, 1):
        clue_data[i].text = "{} {}".format(indicator[j], menu_options[j])               # Set text lines
        j += 1
    clue_data[maxLineLen].text = "File {} of {}".format((selected + 1), max_length)     # Set location text
    clue_data.show()                                                                    # Show text on display

    # Check for button press events
    '''
    press
    A & B - Show terminal
      A   - Move down one
      B   - Run selected file
    '''
    if clue.button_a and clue.button_b:                
        clue_data.show_terminal()           # simply_text_display and show terminal while both buttons are pressed
        time.sleep(0.1)                     # Give user some time to let go
    elif clue.button_a:
        move_count += 1                                 # Change move_count
        selected = move_count % max_length              # Get remainder only after dividing move_count and max_length
        if selected > (start_pos + maxLineLen - 1):     # When the selected position is at end of display move list up by one
            start_pos += 1
        elif selected < start_pos:                      # When the selected position loops, reset start_pos
            start_pos = 0
        time.sleep(0.1)                                 # Give user some time to let go
    elif clue.button_b:
        countdown(2)                                    # Start countdown
        clue_data.show_terminal()                       # Show terminal
        exec(open(menu_options[selected]).read())       # Run selected program
        time.sleep(1)                                   # Give the user time to read terminal one last time