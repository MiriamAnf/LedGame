import neopixel
import machine
from random import randrange

class LedRGB:
    def __init__(self):
        self.np = neopixel.NeoPixel(machine.Pin(27), 1)
        self.temporizador = machine.Timer(-1)

    def encender(self):
        self.np[0] = (self.color_aleatorio())
        self.np.write() 

    def apagar(self):
        self.np[0] = (0, 0, 0)
        self.np.write()  

    @staticmethod
    def color_aleatorio():
        r = randrange(0, 255)
        g = randrange(0, 255)
        b = randrange(0, 255)
        return r, g, b

class Button:
    def __init__(self, pinNumber):
        self.flag = False
        self.button = machine.Pin(pinNumber, machine.Pin.IN)
        self.button.irq(self.cb, machine.Pin.IRQ_FALLING)
                
    def cb(self, ins):
        self.flag = True

    def get_pulsado(self):
        if not self.flag: 
            return False
        self.flag = False
        return True              
