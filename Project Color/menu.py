from time import sleep
from sense_hat import SenseHat
import random

w = (255, 255, 255)

sense = SenseHat()
sense.clear()

sense.set_pixel(7, 2, w)
sense.set_pixel(7, 3, w)
sense.set_pixel(7, 1, w)
sense.set_pixel(6, 1, w)
sense.set_pixel(5, 1, w)
sense.set_pixel(5, 2, w)
sense.set_pixel(5, 3, w)

sense.set_pixel(0, 1, w)
sense.set_pixel(1, 1, w)
sense.set_pixel(2, 1, w)
sense.set_pixel(3, 1, w)
sense.set_pixel(3, 2, w)
sense.set_pixel(3, 3, w)
sense.set_pixel(2, 3, w)
sense.set_pixel(1, 3, w)
sense.set_pixel(1, 2, w)

sense.set_pixel(2, 7, w)
sense.set_pixel(2, 6, w)
sense.set_pixel(2, 5, w)
sense.set_pixel(3, 7, w)
sense.set_pixel(4, 7, w)
sense.set_pixel(4, 6, w)
sense.set_pixel(4, 5, w)
sense.set_pixel(5, 5, w)
sense.set_pixel(6, 7, w)
sense.set_pixel(6, 6, w)
sense.set_pixel(6, 5, w)

for event in sense.stick.get_events():
    if event.action == "pressed":
        if event.direction == "up":
            import Pong
        elif event.direction == "down":
            open("Pong.py")
        elif event.direction == "right":
            open("Snake.py")
