from Sensors import *
from CompositeLights import *

class MotionSensor(DigitalSensor):
    
    def __init__(self, pin):
        super().__init__(pin, lowactive=False)
        
    def motionDetected(self):
        return self.tripped()
    
class PartyLight:
    
    def __init__(self, npin):
            self._pin = npin
            self._neo = NeoPixel(pin=self._pin, numleds=16, brightness=1)
            
    def on(self):
        self._neo.on()
                
    def on(self):
        self._neo.off()
        
    def disco(self):
        self._neo.run(2)