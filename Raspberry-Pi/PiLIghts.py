# Name: Nathan Arter Nov 11 2020
# Last Updates: Nov 11 9:42pm
# Description: Xmas light show for the Pi

# Import this stuff so you can control the pins and you can sleep your program
from gpiozero import LED
from time import sleep

# these are the gpio pins so you know were to plug the ssr in at
redpin = LED(17)
bluepin = LED(27)
greenpin = LED(22)


# # making it easier to turn the red lights on
def red():
    redpin.on()
    sleep(1)
    redpin.off()


# making it easier to turn the blue lights on
def blue():
    bluepin.on()
    sleep(1)
    bluepin.off()


# making it easier to turn the green lights on
def green():
    greenpin.on()
    sleep(1)
    greenpin.off()


green()