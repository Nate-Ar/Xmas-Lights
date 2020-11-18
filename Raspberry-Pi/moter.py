from gpiozero import Servo
from time import sleep


def arm():
    servo = Servo(4)
    servo.min()
    sleep(2)
    servo.max()
    sleep(2)
    servo.mid()
    sleep(1)

while True:
    inputs = input(">  ")

    if inputs == "arm":
        arm()
    if inputs == "exit":
        break