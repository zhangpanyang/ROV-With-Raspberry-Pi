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
from laserTask import readLaserSensor
from pressTask import readPressureSensor
from cameraTask import capture_image

from vars import pi

motorTest3 = Motor(26, 21)
motorTest2 = Motor(13, 19)
motorTest1 = Motor(5, 6)

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

while True:
    laserDistance, laserStrength, laserTemp = readLaserSensor()
    pressureValue, pressureTemp = readPressureSensor()

    for keyHandler in keyHandlers:
        keyHandler.handle()
        # print(keyHandler.pin, keyHandler.state)
    if keyHandlers[0].state:
        motorTest1.setSpeed(0.5)
    elif keyHandlers[1].state:
        motorTest1.setSpeed(-0.5)
    else:
        motorTest1.setSpeed(0)
    if keyHandlers[3].newDown:
        print('newdown')
        now = datetime.now()
        timeDisplayStr = now.strftime("%Y-%m-%d %H:%M:%S")
        timeFilenameStr = now.strftime("%Y-%m-%d_%H-%M-%S_%f")
        displayStr = timeDisplayStr + f', Distance: {laserDistance:.3f}m, Pressure: {pressureValue:.3f}, Temperature: {pressureTemp:.3f}C'
        capture_image("capture/"+timeFilenameStr+".png", displayStr)

    # print(f'Distance: {laserDistance:.3f}m, pressure: {pressureValue:.3f}, temperature: {pressureTemp:.3f}C')

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
