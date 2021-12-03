from time import sleep
from sense_hat import SenseHat
import random

gameStarted = False

# Define some colors
r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
y = (255, 255, 0)

sense = SenseHat()
sense.clear()

# Color Red Part
sense.set_pixel(3, 0, r)
sense.set_pixel(4, 0, (r))
sense.set_pixel(3, 1, (r))
sense.set_pixel(4, 1, (r))

# Color Blue Part
sense.set_pixel(0, 3, (b))
sense.set_pixel(0, 4, (b))
sense.set_pixel(1, 3, (b))
sense.set_pixel(1, 4, (b))

# Color Green Part
sense.set_pixel(3, 7, (g))
sense.set_pixel(3, 6, (g))
sense.set_pixel(4, 6, (g))
sense.set_pixel(4, 7, (g))

# Color Yellow Part
sense.set_pixel(6, 3, (y))
sense.set_pixel(6, 4, (y))
sense.set_pixel(7, 3, (y))
sense.set_pixel(7, 4, (y))

counter = 3


# For the middle

def displayColor():
    colorsId = []
    colorsTreated = 0
    while (colorsTreated < counter):
        nbrandom = random.randint(1, 4)
        colorsId.append(nbrandom)
        colorsTreated += 1
    for id in colorsId:
        if id == 1:
            sense.set_pixel(3, 3, r)
            sense.set_pixel(3, 4, r)
            sense.set_pixel(4, 3, r)
            sense.set_pixel(4, 4, r)
        elif id == 2:
            sense.set_pixel(3, 3, g)
            sense.set_pixel(3, 4, g)
            sense.set_pixel(4, 3, g)
            sense.set_pixel(4, 4, g)
        elif id == 3:
            sense.set_pixel(3, 3, b)
            sense.set_pixel(3, 4, b)
            sense.set_pixel(4, 3, b)
            sense.set_pixel(4, 4, b)
        else:
            sense.set_pixel(3, 3, y)
            sense.set_pixel(3, 4, y)
            sense.set_pixel(4, 3, y)
            sense.set_pixel(4, 4, y)
        sleep(1)

while True:
    for event in sense.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed":
            if event.direction == "middle":
                sense.show_letter("M")  # Enter key
                if not gameStarted:
                    gameStarted = True

while gameStarted:
    displayColor()

