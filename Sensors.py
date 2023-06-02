from machine import Pin, ADC
class Sensor:
        
    def __init__(self, pin, lowactive = True):
        self._pin = pin
        self._lowactive = lowactive
        
    def tripped(self)->bool:
        print(f"tripped not implemented for {type(self).__name__}")
        return False
class DigitalSensor(Sensor):
        
    def __init__(self, pin, lowactive=True):
        super().__init__(pin, lowactive)
        self._pinio = Pin(self._pin, Pin.IN)
    def tripped(self)->bool:
        v = self._pinio.value()
        if (self._lowactive and v == 0) or (not self._lowactive and v == 1):
            print("DigitalLightSensor: sensor tripped")
            return True
        else:
            return False
class AnalogSensor(Sensor):
        
    def __init__(self, pin, lowactive=True, threshold = 30000):
                
        super().__init__(pin, lowactive)
        self._pinio = ADC(self._pin)
        self._threshold = threshold
    def tripped(self)->bool:
                
        v = self.rawValue()
        if (self._lowactive and v < self._threshold) or (not self._lowactive and v > self._threshold):
            print("AnalogLightSensor: sensor tripped")
            return True
        else:
            return False
    def rawValue(self):
        return self._pinio.read_u16()