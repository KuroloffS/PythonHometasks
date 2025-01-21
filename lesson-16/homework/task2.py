import numpy as np

def calculate_power(base, exponent):
    """
    Calculate the power of a number.

    Parameters:
    base (float): The base number.
    exponent (float): The exponent.

    Returns:
    float: The result of base raised to the power of exponent.
    """
    return base ** exponent

# Arrays for base numbers and exponents
bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])

# Vectorize the power calculation function
vectorized_power = np.vectorize(calculate_power, otypes=[float])

# Apply the vectorized function to the arrays
powers = vectorized_power(bases, exponents)

print("Powers:")
for b, e, p in zip(bases, exponents, powers):
    print(f"{b}^{e} = {p:.2f}")
