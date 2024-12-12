from vars import pi

class Motor:
    def __init__(self, pin1, pin2):
        self._frequency = 1000
        self.pin1 = pin1
        self.pin2 = pin2
        pi.set_PWM_frequency(pin1, self._frequency)
        pi.set_PWM_dutycycle(pin1, 255)
        pi.set_PWM_frequency(pin2, self._frequency)
        pi.set_PWM_dutycycle(pin2, 255)
    
    def setSpeed(self, speed):
        if abs(speed) > 1:
            return
        
        if speed >= 0:
            pi.set_PWM_dutycycle(self.pin1, 255)
            pi.set_PWM_dutycycle(self.pin2, round(255*(1-speed)))
        else:
            pi.set_PWM_dutycycle(self.pin1, round(255*(1+speed)))
            pi.set_PWM_dutycycle(self.pin2, 255)