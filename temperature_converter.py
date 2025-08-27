"""Temperature converter"""

def celsius_to_fahrenheit(grads):
    fahrenheit = int(grads) * (9 / 5) + 32
    print(f"{fahrenheit}°")

celsius_to_fahrenheit(input("Celsius grads to convert: "))