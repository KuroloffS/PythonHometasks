import matplotlib.pyplot as plt
import numpy as np

# Define the function
def quadratic_function(x):
    """Calculate the quadratic function f(x) = x^2 - 4x + 4."""
    return x**2 - 4 * x + 4

try:
    # Generate x values
    x_values = np.linspace(-10, 10, 500)  # 500 points for smooth plotting

    # Calculate y values
    y_values = quadratic_function(x_values)

    # Create the plot
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label=r"$f(x) = x^2 - 4x + 4$", color="blue")

    # Customize the plot
    plt.title("Plot of $f(x) = x^2 - 4x + 4$", fontsize=14)
    plt.xlabel("x", fontsize=12)
    plt.ylabel("f(x)", fontsize=12)
    plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
    plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
    plt.grid(alpha=0.3)
    plt.legend(fontsize=12)

    # Show the plot
    plt.show()

except Exception as e:
    print(f"An error occurred: {e}")
