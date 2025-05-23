# **CREATE Phase: Homework Problem Set**

# **Problem 1: Simple Temperature Converter**
# *   **Task:** Write a Python script that includes two functions:
#     1.  `celsius_to_fahrenheit(celsius)`: Takes a temperature in Celsius (float) and returns the equivalent in Fahrenheit (float). Formula: `F = C * 9/5 + 32`.
#     2.  `fahrenheit_to_celsius(fahrenheit)`: Takes a temperature in Fahrenheit (float) and returns the equivalent in Celsius (float). Formula: `C = (F - 32) * 5/9`.
# *   **Main Script:**
#     *   Prompt the user to enter a temperature and its unit (C or F).
#     *   Call the appropriate function to convert it.
#     *   Print the original and converted temperatures neatly.
#     *   Example: "25.0°C is 77.0°F" or "68.0°F is 20.0°C".

def convertTemp(unit, temp):
    # unit = input(f'Enter unit: ')
    # temp = float(input(f'Enter temp: '))
    x = 0
    if unit.capitalize() == 'C':
        # x = celsius_to_fahrenheit(temp)
        x = (lambda x: (x * 9/5) + 32)(temp)
        print(f'{temp} celsius is {x} fahrenheit.')
    else:
        # x = fahrenheit_to_celsius(temp)
        x = (lambda x: (x - 32) * 5/9)(temp)
        print(f'{temp} fahrenheit is {x} celsius.')
        
def celsius_to_fahrenheit(temp):  
    print('Calculating F') 
    return (temp * 9/5) + 32

def fahrenheit_to_celsius(temp):
    print('Calculating C') 
    return (temp - 32) * 5/9
   
# unit = input(f'Enter unit: '), 
# temp = float(input(f'Enter temp: '))
convertTemp('C', 50)

