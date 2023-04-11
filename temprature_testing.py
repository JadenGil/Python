from temperature import TemperatureError, Temperature

"""
This file is for testing all of the features of the Temperature class

If you run into errors, consider using the debugger to trace through your code
Utilize breakpoints to help you find the errors more quickly
"""

VALID_TEMPERATURES = [-45, 55.2, "-14.75", "34C", "3.4C", "-10.2C",
                      "-11.2F", "23.5F", "74.5F", "245.3K"]
INVALID_TEMPERATURES = ["garbage", "34 degrees celsius", [], "45P", "34CC",
                        {"C": 23}]


# Creating some valid temperatures
temperatures = []
for value in VALID_TEMPERATURES:
    try:
        temperatures.append(Temperature(value))
    except Exception as e:
        print(e, 'occurred when initializing a Temperature for value', value)
print()

print('Testing the getters')
print('inputted:', VALID_TEMPERATURES)
try:
    print('result in Celsius:', [temperature.celsius for temperature in temperatures])
    print('result in Kelvin:', [temperature.kelvin for temperature in temperatures])
    print('result in Fahrenheit:', [temperature.fahrenheit for temperature in temperatures])
except Exception as e:
    print(e, 'occurred when utilizing getters')
print()

# Computing the average of the values
print('The average of those temps is', Temperature.average(temperatures).celsius)
print('This should be approx. -1.0311')
print()

# Creating invalid temperatures
# All should raise TemperatureErrors
print('Trying to initialize with bad values')
for value in INVALID_TEMPERATURES:
    try:
        Temperature(value)
    except TemperatureError:
        print('Correct error raised for', value)
    except Exception as e:
        print(e, 'raised instead of TemperatureError for', value)
print()


print('Testing the setters')
print('Each of these values should be 0.0:')
try:
    a = Temperature()
    a.kelvin = 273.15
    print(a.celsius)
    a.kelvin = '273.15K'
    print(a.celsius)
    a.kelvin = '273.15'
    print(a.celsius)
    a.fahrenheit = 32.0
    print(a.celsius)
    a.fahrenheit = '32F'
    print(a.celsius)
    a.fahrenheit = '32'
    print(a.celsius)
    a.celsius = '0C'
    print(a.celsius)
    a.celsius = 0
    print(a.celsius)
    a.celsius = '0'
    print(a.celsius)
except Exception as e:
    print(e, 'occurred when testing setters')
