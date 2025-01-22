import matplotlib.pyplot as plt
import numpy as np

# Define the functions
def cubic_function(x):
    """Calculate f(x) = x^3."""
    return x**3

def exponential_function(x):
    """Calculate f(x) = e^x."""
    return np.exp(x)

def logarithmic_function(x):
    """Calculate f(x) = log(x + 1)."""
    return np.log(x + 1)

try:
    # Generate x values
    x_cubic = np.linspace(-10, 10, 500)  # For cubic function
    x_sine = np.linspace(0, 2 * np.pi, 500)  # For sine function
    x_exponential = np.linspace(-2, 2, 500)  # For exponential function
    x_logarithmic = np.linspace(0, 10, 500)  # For logarithmic function (x >= 0)

    # Calculate y values
    y_cubic = cubic_function(x_cubic)
    y_sine = np.sin(x_sine)
    y_exponential = exponential_function(x_exponential)
    y_logarithmic = logarithmic_function(x_logarithmic)

    # Create subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle("2x2 Grid of Functions", fontsize=16)

    # Top-left: Cubic function
    axs[0, 0].plot(x_cubic, y_cubic, color="purple")
    axs[0, 0].set_title(r"$f(x) = x^3$", fontsize=14)
    axs[0, 0].set_xlabel("x", fontsize=12)
    axs[0, 0].set_ylabel("f(x)", fontsize=12)
    axs[0, 0].grid(alpha=0.3)

    # Top-right: Sine function
    axs[0, 1].plot(x_sine, y_sine, color="blue")
    axs[0, 1].set_title(r"$f(x) = \sin(x)$", fontsize=14)
    axs[0, 1].set_xlabel("x", fontsize=12)
    axs[0, 1].set_ylabel("f(x)", fontsize=12)
    axs[0, 1].grid(alpha=0.3)

    # Bottom-left: Exponential function
    axs[1, 0].plot(x_exponential, y_exponential, color="green")
    axs[1, 0].set_title(r"$f(x) = e^x$", fontsize=14)
    axs[1, 0].set_xlabel("x", fontsize=12)
    axs[1, 0].set_ylabel("f(x)", fontsize=12)
    axs[1, 0].grid(alpha=0.3)

    # Bottom-right: Logarithmic function
    axs[1, 1].plot(x_logarithmic, y_logarithmic, color="orange")
    axs[1, 1].set_title(r"$f(x) = \log(x+1)$", fontsize=14)
    axs[1, 1].set_xlabel("x", fontsize=12)
    axs[1, 1].set_ylabel("f(x)", fontsize=12)
    axs[1, 1].grid(alpha=0.3)

    # Adjust layout
    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust for the main title
    plt.show()

except Exception as e:
    print(f"An error occurred: {e}")
