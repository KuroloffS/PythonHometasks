import numpy as np

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.

    Parameters:
    fahrenheit (float): Temperature in Fahrenheit.

    Returns:
    float: Temperature in Celsius.

    Raises:
    ValueError: If the input is not a number.
    """
    try:
        return (float(fahrenheit) - 32) * 5 / 9
    except ValueError:
        raise ValueError(f"Invalid input: {fahrenheit} is not a number.")

# Predefined temperatures in Fahrenheit
temperatures_fahrenheit = np.array([32, 68, 100, 212, 77])

# Vectorize the conversion function
vectorized_conversion = np.vectorize(fahrenheit_to_celsius, otypes=[float])

# Apply the vectorized function to the array
temperatures_celsius = vectorized_conversion(temperatures_fahrenheit)

print("\nTemperatures:")
for f, c in zip(temperatures_fahrenheit, temperatures_celsius):
    print(f"{f}°F = {c:.2f}°C")
