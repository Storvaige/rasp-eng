from sense_hat import SenseHat
import time
import random
    
senseHat = SenseHat()
senseHat.low_light = True
    
GREEN = (0, 255, 0)
RED = (255, 0, 0)
START_DELAY = 3
MATRIX_MIN_VALUE = 0
MATRIX_MAX_VALUE = 7
MATRIX_SIZE = 8
    
while True:
    #Variables
    gameOverFlag = False
    growSnakeFlag = False
    generateRandomFoodFlag = False
    snakeMovementDelay = 0.5
    snakeMovementDelayDecrease = -0.02

    #Start delayQ
    time.sleep(START_DELAY)

    #Position of the start
    snakePosX = [3]
    snakePosY = [6]

    #Position of pixel random
    while True:
        foodPosX = random.randint(0, 7)
        foodPosY = random.randint(0, 7)
        if foodPosX != snakePosX[0] or foodPosY != snakePosY[0]:
            break

    #Random direction for the snake
    movementX = 0
    movementY = -1

    # -----------------------------------
    #              Loop
    # -----------------------------------
    while not gameOverFlag:
        #Eat pixel
        if foodPosX == snakePosX[0] and foodPosY == snakePosY[0]:
            growSnakeFlag = True
            generateRandomFoodFlag = True
            snakeMovementDelay += snakeMovementDelayDecrease

        #If Snake eat itself = Lose
        for i in range(1, len(snakePosX)):
            if snakePosX[i] == snakePosX[0] and snakePosY[i] == snakePosY[0]:
                gameOverFlag = True

        #Game Over
        if gameOverFlag:
            sense.show_message("You Lose", text_colour=(255, 0, 0))
            break

        #Use the joystick
        events = senseHat.stick.get_events()
        for event in events:
            if event.direction == "left" and movementX != 1:
                movementX = -1
                movementY = 0
            elif event.direction == "right" and movementX != -1:
                movementX = 1
                movementY = 0
            elif event.direction == "up" and movementY != 1:
                movementY = -1
                movementX = 0
            elif event.direction == "down" and movementY != -1:
                movementY = 1
                movementX = 0

        #+1 when you eat Pixel
        if growSnakeFlag:
            growSnakeFlag = False
            snakePosX.append(0)
            snakePosY.append(0)

        #Movement
        for i in range((len(snakePosX) - 1), 0, -1):
            snakePosX[i] = snakePosX[i - 1]
            snakePosY[i] = snakePosY[i - 1]

        snakePosX[0] += movementX
        snakePosY[0] += movementY

        #Border of the game
        if snakePosX[0] > MATRIX_MAX_VALUE:
            snakePosX[0] -= MATRIX_SIZE
        elif snakePosX[0] < MATRIX_MIN_VALUE:
            snakePosX[0] += MATRIX_SIZE
        if snakePosY[0] > MATRIX_MAX_VALUE:
            snakePosY[0] -= MATRIX_SIZE
        elif snakePosY[0] < MATRIX_MIN_VALUE:
            snakePosY[0] += MATRIX_SIZE

        #Spawn pixel randomly
        if generateRandomFoodFlag:
            generateRandomFoodFlag = False
            retryFlag = True
            while retryFlag:
                foodPosX = random.randint(0, 7)
                foodPosY = random.randint(0, 7)
                retryFlag = False
                for x, y in zip(snakePosX, snakePosY):
                    if x == foodPosX and y == foodPosY:
                        retryFlag = True
                        break

        #Update
        senseHat.clear()
        senseHat.set_pixel(foodPosX, foodPosY, RED)
        for x, y in zip(snakePosX, snakePosY):
            senseHat.set_pixel(x, y, GREEN)

        #Speed for the snack (Because it's very easy ^^)
        time.sleep(snakeMovementDelay)