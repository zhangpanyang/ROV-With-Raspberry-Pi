import pigpio
import time
from datetime import datetime

import vars

vars.pi = pigpio.pi()
if not vars.pi.connected:
    raise Exception("Failed to connect to pigpio")

from keyTask import ClickType
from keyTask import KeyHandler
from motorTask import Motor
from servoTask import Servo
from laserTask import readLaserSensor
from pressTask import readPressureSensor
from cameraTask import capture_image

from vars import pi

motorTest3 = Motor(26, 21)
motorTest2 = Motor(13, 19)
motorTest1 = Motor(5, 6)
servoBuoyant = Servo(24)

# 3.3V
pi.set_mode(12, pigpio.OUTPUT)
pi.write(12, 1)
pi.set_mode(18, pigpio.OUTPUT)
pi.write(18, 1)

# Control pins
# controlStates = [0, 0, 0, 0]
# controlPins = (4, 17,27,22)
# for pin in controlPins:
#     pi.set_mode(pin, pigpio.INPUT)
#     pi.set_pull_up_down(pin, pigpio.PUD_DOWN)
keyHandlers = []
keyHandlers.append(KeyHandler(4))
keyHandlers.append(KeyHandler(17))
keyHandlers.append(KeyHandler(22))
keyHandlers.append(KeyHandler(27))

laserDistance, laserStrength, laserTemp, pressureValue, pressureTemp = 0, 0, 0, 0, 0

while True:
    try:
        laserDistance, laserStrength, laserTemp = readLaserSensor()
        pressureValue, pressureTemp = readPressureSensor()
    except:
        pass

    for keyHandler in keyHandlers:
        keyHandler.handle()
        # print(keyHandler.pin, keyHandler.state)
    
    # print(keyHandlers[0].state, keyHandlers[1].state, keyHandlers[2].state, keyHandlers[3].state)
    buoyantSpeed = 0
    thrustLeft = 0
    thrustRight = 0
    if keyHandlers[2].state:
        if keyHandlers[0].state:
            buoyantSpeed = 1
        elif keyHandlers[1].state:
            buoyantSpeed = -1
        else:
            thrustLeft = 0.1
            thrustRight = 0.1
    else:
        if keyHandlers[0].state:
            thrustLeft = -0.1
            thrustRight = 0.1
        elif keyHandlers[1].state:
            thrustLeft = 0.1
            thrustRight = -0.1
        else:
            pass
    
    servoBuoyant.setSpeed(buoyantSpeed)
    motorTest1.setSpeed(-thrustLeft)
    motorTest3.setSpeed(thrustRight)
    if keyHandlers[3].newDown:
        print('newdown')
        now = datetime.now()
        timeDisplayStr = now.strftime("%Y-%m-%d %H:%M:%S")
        timeFilenameStr = now.strftime("%Y-%m-%d_%H-%M-%S_%f")
        displayStr = timeDisplayStr + f', Distance: {laserDistance:.3f}m, Pressure: {pressureValue:.3f}, Temperature: {pressureTemp:.3f}C'
        print(displayStr)
        capture_image("capture/"+timeFilenameStr+".png", displayStr)

    time.sleep(0.01)
    # for i in range(-10, 10):
    #     motorTest1.setSpeed(i/100)
    #     motorTest2.setSpeed(i/100)
    #     motorTest3.setSpeed(i/100)
    #     time.sleep(0.4)
    # for i in range(10, -10, -1):
    #     motorTest1.setSpeed(i/100)
    #     motorTest2.setSpeed(i/100)
    #     motorTest3.setSpeed(i/100)
    #     time.sleep(0.4)
