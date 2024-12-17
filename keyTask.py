from vars import pi
from enum import Enum

class ClickType(Enum):
    single = 0
    double = 1

doubleClickInterval = 50

class KeyHandler:
    def __init__(self, pin):
        self.state = 0
        self.clickType = ClickType.single
        self.pin = pin

        self.newDown = False
        self.newUp = False

        self.stemp = 0
        self.lastDownStemp = 0
        self.lastUpStemp = 0
        pass

    def handle(self):
        # Time Stemp
        self.stemp += 1

        prevState = self.state
        self.state = pi.read(self.pin)

        if not prevState and self.state:
            if self.stemp - self.lastUpStemp < 50:
                self.clickType = ClickType.double
            else:
                self.clickType = ClickType.single
            
            self.newDown = True
            self.lastDownStemp = self.stemp

        else:
            self.newDown = False
        
        if prevState and not self.state:
            self.newUp = True
            self.lastUpStemp = self.stemp

        else:
            self.newUp = False