# Name: Nathan Arter Nov 11 2020
# Last Updates: Nov 11 9:42pm
# Description: Xmas light show for the Pi

# Import this stuff so you can control the pins and you can sleep your program
from gpiozero import LED
import os
from time import sleep

# on and off

def slot1(x):
    slot1 = LED(4)
    slot1.on()
    sleep(x)
    slot1.off()
def slot2(x):
    slot2 = LED(17)
    slot2.on()
    sleep(x)
    slot2.off()
def slot3(x):
    slot3 = LED(27)
    slot3.on()
    sleep(x)
    slot3.off()
def slot4(x):
    slot4 = LED(22)
    slot4.on()
    sleep(x)
    slot4.off()
def slot5(x):
    slot5 = LED(5)
    slot5.on()
    sleep(x)
    slot5.off()
def slot6(x):
    slot6 = LED(6)
    slot6.on()
    sleep(x)
    slot6.off()
def slot7(x):
    slot7 = LED(13)
    slot7.on()
    sleep(x)
    slot7.off()
def slot8(x):
    slot8 = LED(19)
    slot8.on()
    sleep(x)
    slot8.off()

# songs
def song1():
    while True:
        slot8(.5)
        sleep(.5)
        slot7(.5)
        sleep(.5)
        slot6(.5)
        sleep(.5)
        slot5(.5)
        sleep(.5)

# run
song1()
