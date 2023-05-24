# Imports go at the top
from microbit import *

"""
Set everything up so:

If the user clicks on the right button - I will add one pixel of the light
Elif the user clicks on the left button - I will remove one pixel of the light

--------------------------------------------------------------------------------

Everything will be controled by gyroscope like: 
    1. If the user turns the chip on the right, lights are going to the right corner
        ----- exception: if there are no place to go to the right then a sound will play
    2. If the user turns the chip on the left, lights are going to the left corner
        ----- exception: if there are no place to go to the left then a sound will play
        !!!! simple solution: add counter var which -= 1 and += 1
    3. If the user decides to turn the chip on the top, lights are going to the top 
        ----- exception; if there are no place to go to the top, the a sound will play
    4. If the user decides to turn the chip on the bottom, lights are going to the bottom
        ----- exception; if there are no place to go to the bottom, the a sound will play
        !!!! simple solution: add counter var which -= 1 and += 1
"""


i = 2
j = 2
while True:

    click__counter = 2
    display.set_pixel(i, 2, 9)

    if button_b.is_pressed():
        i += 1
        display.set_pixel(i, 2, 9)
        sleep(200)
    elif button_a.is_pressed():
        j -= 1
        display.set_pixel(j, 2, 9)
        sleep(200)

    """elif button_a.is_pressed() and button_b.is_pressed():
        display.clear()
        display.show(Image('00300:'
                           '03630:'
                           '36963:'
                           '03630:'
                           '00300'))"""
