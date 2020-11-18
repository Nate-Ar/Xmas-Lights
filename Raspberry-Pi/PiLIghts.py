# Name: Nathan Arter Nov 11 2020
# Last Updates: Nov 11 9:42pm
# Description: Xmas light show for the Pi

# Import this stuff so you can control the pins and you can sleep your program
from gpiozero import LED
import os
from time import sleep

# these are the gpio pins so you know were to plug the ssr in at
slot1 = LED(4)
slot2 = LED(17)
slot3 = LED(27)
slot4 = LED(22)
slot5 = LED(5)
slot6 = LED(6)
slot7 = LED(13)
slot8 = LED(19)


def song1():
    os.system('mpg321 song1.mp3 &')

song1()