import unittest
from temperature import Temperature, TemperatureError
import sys

t1=Temperature(22)
print(t1.celsius)
print(t1.farenheit)
t1.celsius=30.0
print(t1.celsius)
print(t1.farenheit)
t1.farenheit=90
print(t1.celsius)
print(t1.farenheit)
