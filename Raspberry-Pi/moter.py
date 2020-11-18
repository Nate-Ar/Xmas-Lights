from gpiozero import Servo
from time import sleep

servo = Servo(4)


def arm():
    servo.max()
    sleep(1)
    servo.mid()
    sleep(1)





arm()