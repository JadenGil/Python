"""Tools for working with Temperatures."""


class Temperature:
    """Represents a temperature."""

    def __init__(self, degrees=0):
        """Initialize temperature with specified degrees celsius.

        Args:
            degrees: number of degrees celsius
 
        """
        self.celsius = degrees

    def __float__(self):
      return float(self.celsius)

    def __eq__(self,other):
      return float(self) == float(other)



t1=Temperature(34)
print(t1==45)
