import numpy as np

# Coefficients matrix for the circuit equations
coefficients = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])

# Constants vector
constants = np.array([12, -5, 15])

# Solve the system of equations for currents
try:
    currents = np.linalg.solve(coefficients, constants)
    print("Currents in the circuit:")
    print(f"I_1 = {currents[0]:.2f} A")
    print(f"I_2 = {currents[1]:.2f} A")
    print(f"I_3 = {currents[2]:.2f} A")
except np.linalg.LinAlgError as e:
    print("Error:", e)
