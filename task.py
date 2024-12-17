import pigpio
import time

import vars

vars.pi = pigpio.pi()
if not vars.pi.connected:
    raise Exception("Failed to connect to pigpio")

from motorTask import Motor
from laserTask import readLaserSensor
from pressTask import readPressureSensor

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
controlStates = [0, 0, 0, 0]
controlPins = (4, 17,27,22)
for pin in controlPins:
    pi.set_mode(pin, pigpio.INPUT)
    pi.set_pull_up_down(pin, pigpio.PUD_DOWN)

while True:
    for i in range(0,4):
        controlStates[i] = pi.read(controlPins[i])
    if controlStates[0]:
        motorTest1.setSpeed(0.1)
    else:
        motorTest1.setSpeed(0)

    # laserDistance, laserStrength, laserTemp = readLaserSensor()
    # pressureValue, pressureTemp = readPressureSensor()
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
