#clue_menu.py
# CircuitPython Clue Cutebot
# Last upDated July 23, 2020
# Author(s): James Tobin

######################################################
#   Import
######################################################
import time
import os
#import cutebot
#from cutebot import clue
from adafruit_clue import clue



######################################################
#   Global Variables
######################################################
arrow = '->'
selected = 0
move_count = 0
hidden_ID = ['.', 'TRASH']
small_text_mode = True
start = 0
b = 0

######################################################
#   Functions
######################################################
def file_filter(data):
    #for y in hidden_ID:
    for y in hidden_ID:
        filtered_data = [x for x in data if not x.startswith(y)]
        data = filtered_data
    filtered_data = [x for x in data if x[-3:] == '.py']
    return sorted(filtered_data)

def countdown(duration):
    duration = max(duration, 1)
    duration/=4
    clue_data[0].text = '1'
    clue_data.show()
    clue.play_tone(1046.5,duration)
    clue_data[0].text = '2'
    clue_data.show()
    clue.play_tone(1147.7,duration)
    clue_data[0].text = '3'
    clue_data.show()
    clue.play_tone(1568,(duration*2))


######################################################
#   Main Code
######################################################
print("\nPRESS A BUTTON AT STARTUP TO ENTER SMALL TEXT MODE\n.")
time.sleep(1.5)
if clue.button_a:
    small_text_mode = True
else:
    small_text_mode = False 

menu_options = file_filter(os.listdir())
indicator = ['  '] * len(menu_options)
indicator[selected] = arrow # set arrows first location

#Create a simple_text_display
if small_text_mode == True:
    clue_data = clue.simple_text_display(title="Menu", title_scale=2, text_scale=1)
    maxLineLen = 15
else:
    clue_data = clue.simple_text_display(title="Menu", title_scale=3, text_scale=2)
    maxLineLen = 6

if len(menu_options) < maxLineLen:
    maxLineLen = len(menu_options)

while True:
    '''
    '''
    indicator = ['  '] * len(menu_options)
    indicator[selected] = arrow
    j = start
    for i in range(0, maxLineLen, 1):
        clue_data[i].text = "{} {}".format(indicator[j], menu_options[j])
        j += 1
    clue_data[maxLineLen].text = "Item {} of {}".format((selected + 1), len(menu_options))
    clue_data.show()
    if clue.button_a:
        move_count += 1
        selected = move_count % len(menu_options)
        if selected > (start + maxLineLen - 1):
            start += 1
        elif selected < start:
            start = 0
        b = start + maxLineLen
        time.sleep(0.1)
    if clue.button_b:
        countdown(2)
        clue_data.show_terminal()
        exec(open(menu_options[selected]).read())

print("END") 