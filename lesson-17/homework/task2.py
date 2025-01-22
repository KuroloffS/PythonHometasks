import matplotlib.pyplot as plt
import numpy as np

# Define sine and cosine functions
def sine_function(x):
    """Calculate the sine function."""
    return np.sin(x)

def cosine_function(x):
    """Calculate the cosine function."""
    return np.cos(x)

try:
    # Generate x values
    x_values = np.linspace(0, 2 * np.pi, 500)  # 500 points from 0 to 2π

    # Calculate y values for sine and cosine
    sine_values = sine_function(x_values)
    cosine_values = cosine_function(x_values)

    # Create the plot
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, sine_values, label=r"$\sin(x)$", color="blue", linestyle="--")
    plt.plot(x_values, cosine_values, label=r"$\cos(x)$", color="red", linestyle="-.")

    # Customize the plot
    plt.title("Sine and Cosine Functions", fontsize=14)
    plt.xlabel("x (radians)", fontsize=12)
    plt.ylabel("y", fontsize=12)
    plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
    plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
    plt.grid(alpha=0.3)
    plt.legend(fontsize=12)

    # Show the plot
    plt.show()

except Exception as e:
    print(f"An error occurred: {e}")
