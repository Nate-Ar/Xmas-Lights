# Name: Nathan Arter Nov 11 2020
# Last Updates: Nov 11 9:42pm
# Description: Xmas light show for the Pi

# Import this stuff so you can control the pins and you can sleep your program
from gpiozero import LED
import os
from time import sleep
import librosa, librosa.display
from random import randint
import matplotlib.pyplot as plt
import time


def analze(file):
    file = file
    signal, sr = librosa.load(file, sr=22050)
    librosa.display.waveplot(signal, sr=sr)

    y, sr = librosa.load(file)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    return round(tempo/60, 1)

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


def rooftop():
    tempo = analze("UpOnTheRoofTop.wav")
    presec = tempo / 2 - .25
    count = 0
    os.system('mpg321 upOnTheRoofTop.wav &')
    while count <= 216:
        sleep(presec)
        rando = randint(0, 100)
        if rando <= 12:
            slot8(.25)
        if 12 < rando <= 24:
            slot7(.25)
        if 24 < rando <= 36:
            slot6(.25)
        if 36 < rando <= 48:
            slot5(.25)
        if 48 < rando <= 50:
            slot4(.25)
        if 50 < rando <= 62:
            slot3(.25)
        if 62 < rando <= 74:
            slot2(.25)
        if 74 < rando <= 100:
            slot1(.25)
        count += presec


rooftop()
