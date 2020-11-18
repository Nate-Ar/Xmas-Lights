from gpiozero import Servo
from time import sleep

servo = Servo(4)


def arm():
    servo.min()
    sleep(2)
    servo.max()
    sleep(2)
    servo.mid()
    sleep(1)
def spin():
    servo.max()
arm()

