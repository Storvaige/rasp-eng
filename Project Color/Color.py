from time import sleep
from sense_hat import SenseHat
import random

preGame = True
Lost = False

# Define some colors
r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
y = (255, 255, 0)
n = (0, 0, 0)
w = (255, 255, 255)

sense = SenseHat()
sense.clear()

# Color Red Part
sense.set_pixel(3, 0, r)
sense.set_pixel(4, 0, r)
sense.set_pixel(3, 1, r)
sense.set_pixel(4, 1, r)

# Color Blue Part
sense.set_pixel(0, 3, b)
sense.set_pixel(0, 4, b)
sense.set_pixel(1, 3, b)
sense.set_pixel(1, 4, b)

# Color Green Part
sense.set_pixel(3, 7, g)
sense.set_pixel(3, 6, g)
sense.set_pixel(4, 6, g)
sense.set_pixel(4, 7, g)

# Color Yellow Part
sense.set_pixel(6, 3, y)
sense.set_pixel(6, 4, y)
sense.set_pixel(7, 3, y)
sense.set_pixel(7, 4, y)

counter = 3


def middleColor(x):
    sense.set_pixel(3, 3, x)
    sense.set_pixel(3, 4, x)
    sense.set_pixel(4, 3, x)
    sense.set_pixel(4, 4, x)


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
            middleColor(r)
        elif id == 2:
            middleColor(g)
        elif id == 3:
            middleColor(b)
        else:
            middleColor(y)
        sleep(0.8)
        middleColor(n)
        sleep(0.8)

    print(colorsId)
    return colorsId


def receiveInputs(nbInputs):
    nbInputsReceived = 0
    inputsReceived = []
    while nbInputsReceived < nbInputs:
        for event in sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "up":
                    inputsReceived.append(1)
                elif event.direction == "down":
                    inputsReceived.append(2)
                elif event.direction == "left":
                    inputsReceived.append(3)
                elif event.direction == "right":
                    inputsReceived.append(4)

                nbInputsReceived += 1
                middleColor(w)
                sleep(0.2)
                middleColor(n)

    print(inputsReceived)
    return inputsReceived


while preGame:
    for event in sense.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed":
            if event.direction == "middle":
                # Enter key
                preGame = False

if not preGame:
    while not Lost:
        print("colors : " + str(counter))

        generatedColorsId = displayColor()
        receivedColorsId = receiveInputs(counter)

        for index in range(len(generatedColorsId)):
            if generatedColorsId[index] != receivedColorsId[index]:
                Lost = True

        if not Lost:
            counter += 1

print("\n\nGAME OVER\n")
print("Score : " + str(counter-3))
sense.show_message(str(counter-3))