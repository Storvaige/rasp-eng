from time import sleep
from sense_hat import SenseHat
import random

gameStarted = False

#Define some colors
w=(255,255,255)
r=(255,0,0)
g=(0,255,0)
b=(0,0,255)
y=(255,255,0)

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

def middleClear():
  # Color White Middle
  sense.set_pixel(3, 3, w)
  sense.set_pixel(3, 4, w)
  sense.set_pixel(4, 3, w)
  sense.set_pixel(4, 4, w)

counter = 3



counter=3

# For the middle
def displayColor():
  display = counter
  while(display!=0):
    display = display - 1
    nbrandom = random.randint(1, 4)
    if nbrandom == 1:
        sense.set_pixel(3, 3, r)
        sense.set_pixel(3, 4, r)
        sense.set_pixel(4, 3, r)
        sense.set_pixel(4, 4, r)
    elif nbrandom == 2:
        sense.set_pixel(3, 3, g)
        sense.set_pixel(3, 4, g)
        sense.set_pixel(4, 3, g)
        sense.set_pixel(4, 4, g)
    elif nbrandom == 3:
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
    middleClear()
    sleep(1)
  display +=1 
  
while True:
  for event in sense.stick.get_events():
    # Check if the joystick was pressed
    if event.action == "pressed":

      if event.direction == "middle":
        sense.show_letter("M")      # Enter key
        if gameStarted == False:
          gameStarted = True

      if event.direction == "up": #Up = Red
        sense.show_letter("U")      # Enter key
        if gameStarted == True:

          
while gameStarted == True:
  displayColor()
  
