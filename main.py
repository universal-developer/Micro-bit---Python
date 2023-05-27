# Imports go at the top
from microbit import *
import music

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


RIGHT = 2
LEFT = 2


def set_pixels():
    global RIGHT
    global LEFT

    display.set_pixel(RIGHT, 2, 9)

    try:
        if button_b.is_pressed():
            if RIGHT == 4:
                display.show(Image.SAD)
                sleep(200)
                music.play(music.POWER_DOWN)
                display.clear()
                sleep(100)
                RIGHT = 2
            else:
                RIGHT += 1
                display.set_pixel(RIGHT, 2, 9)
                sleep(200)

        elif button_a.is_pressed():
            if LEFT == 0 or LEFT < 0:
                display.show(Image.SAD)
                sleep(200)
                music.play(music.POWER_DOWN)
                display.clear()
                sleep(100)
                LEFT = 2
            else:
                LEFT -= 1
                display.set_pixel(LEFT, 2, 9)
                sleep(200)

    except:
        display.show(Image.SAD)
        sleep(200)
        display.clear()
        sleep(100)
        display.set_pixel(2, 2, 9)


while True:
    set_pixels()
