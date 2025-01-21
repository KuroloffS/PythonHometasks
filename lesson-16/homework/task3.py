import numpy as np

# Coefficients matrix
coefficients = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])

# Constants vector
constants = np.array([7, 4, 5])

# Solve the system of equations
try:
    solution = np.linalg.solve(coefficients, constants)
    print("Solution:")
    print(f"x = {solution[0]:.2f}")
    print(f"y = {solution[1]:.2f}")
    print(f"z = {solution[2]:.2f}")
except np.linalg.LinAlgError as e:
    print("Error:", e)
