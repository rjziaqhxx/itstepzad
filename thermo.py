class Thermostat:
    def __init__(self, temp_cel):
        self._temperature = temp_cel
    
    @property
    def temperature(self):
        """Temperature is in celsius"""
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        if -30 <= value <= 50:
            self._temperature = value
        else:
            raise ValueError('-30  50')
    
    @property
    def fahreinheit(self):
        """Temperature is in fahrenheit"""
        return self._temperature * 9/5 + 32

    @property
    def kelvin(self):
        """Temperature is in kelvin's"""
        return self._temperature + 273.15
    
    @kelvin.setter
    def kelvin(self, value):
        celsius_value = value - 273.15
        if -30 <= celsius_value <= 50:
            self._temperature = celsius_value
        else:
            raise ValueError('-30 50')
        
    @fahreinheit.setter
    def fahreinheit(self, value):
        celsius_value = value/1.8 - 32
        if -30 <= celsius_value <= 50:
            self._temperature = celsius_value
        else:
            raise ValueError('-30 50')
        
    @temperature.deleter
    def temperature(self):
        print('Deleting temp...')
        del self._temperature


obj = Thermostat(15)
print(obj.fahreinheit)
print(obj.kelvin)   

obj.kelvin = 300
print(obj.kelvin)
obj.fahreinheit = 59
print(obj.fahreinheit)

print(Thermostat.temperature.__doc__)