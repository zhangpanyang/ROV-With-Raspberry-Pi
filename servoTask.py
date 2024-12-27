import pigpio
import time
from vars import pi

class Servo:
    def __init__(self, pin):
        self._frequency = 50
        self.pin = pin
        pi.set_PWM_frequency(pin, self._frequency)
        pi.set_PWM_dutycycle(pin, round(255*0.075))
    
    def setSpeed(self, speed):
        if abs(speed) > 1:
            return
        
        pi.set_PWM_dutycycle(self.pin, round(255*(0.075+0.025*speed)))

# servoTest = Servo(24)

# while True:
    # for i in range(-100, 100):
    #     servoTest.setSpeed(i/100)
    #     time.sleep(0.1)
    # for i in range(100, -100, -1):
    #     servoTest.setSpeed(i/100)
    #     time.sleep(0.1)
    # servoTest.setSpeed(1)