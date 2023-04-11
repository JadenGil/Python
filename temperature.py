"""Classes for working with Temperatures."""


class TemperatureError(Exception):
    """Error raised for invalid temperatures."""

    pass


class Temperature:
    """Represents a temperature.

    Temperatures are expressable in degrees Fahrenheit, degrees celsius,
    or Kelvins.
    """

    def __init__(self, degrees=0):
        """Initialize temperature with specified degrees.

        Args:
            degrees, which can be one of the following:
                (1) a number, or a string containing a number
                    in which case it is interpreted as degrees celsius
                (2) a string containing a number followed by one of the
                    following symbols:
                       C, in which case it is interpreted as degrees celsius
                       F, in which case it is interpreted as degrees Fahrenheit
                       K, in which case it is interpreted as Kelvins

        Raises:
            TemperatureError: if degrees is not one of the specified
                                     forms

        """
        if type(degrees)==string:
          self.interpret(self,degrees)
          
        self._celsius= float(degrees)
    def interpret(self,str):
      #return a list with a float  and a letter
    
    def convertF(self):
        tempf=self._celsius *(9/5) + 32
        return  tempf
    def convertCtoF(self,tempc):
        tempf=tempc *(9/5) + 32
        return  tempf
    def convertFtoC(self,tempf):
        tempc=(tempf-32) * (5/9)
        return  tempc
    
    @property
    def celsius(self):
        return  self._celsius

    @celsius.setter
    def celsius(self, temp): 
       self._celsius=float(temp) 
       return  self._celsius
    
    @property
    def farenheit(self):
        return  self.convertCtoF(self._celsius)

    @farenheit.setter
    def farenheit(self,temp): 
        tempc=self.convertFtoC(temp)
        self._celsius=tempc
    
    @classmethod
    def average(cls, temperatures):
        """Compute the average of a list of temperatures.

        Args:
            temperatures: a list of Temperature objects
        Returns:
            a Temperature object with average (mean) of the given temperatures

        """
        pass

