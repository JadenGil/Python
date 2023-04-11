from temperature import Temperature, TemperatureError

"""
This file only tests Celsius functionality

If you run into errors, consider using the debugger to trace through your code
Utilize breakpoints to help you find the errors more quickly
"""

VALID_TEMPERATURES = [-45, 55.2, "-14.75", "34C", "3.4C", "-10.2C"]
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
except Exception as e:
    print(e, 'occurred when utilizing getters')
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
    a.celsius = '0C'
    print(a.celsius)
    a.celsius = 0
    print(a.celsius)
    a.celsius = '0'
    print(a.celsius)
except Exception as e:
    print(e, 'occurred when testing setters')
