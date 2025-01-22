import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_3d_surface():
    try:
        # Define the range for x and y values
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        x, y = np.meshgrid(x, y)

        # Define the function f(x, y) = cos(x^2 + y^2)
        z = np.cos(x**2 + y**2)

        # Create the 3D surface plot
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Plot the surface
        surf = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')

        # Add colorbar
        colorbar = fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)
        colorbar.set_label("Function Value", fontsize=12)

        # Set axis labels and title
        ax.set_title("3D Surface Plot of f(x, y) = cos(x^2 + y^2)", fontsize=14)
        ax.set_xlabel("X-axis", fontsize=12)
        ax.set_ylabel("Y-axis", fontsize=12)
        ax.set_zlabel("Z-axis (f(x, y))", fontsize=12)

        # Show the plot
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to generate the 3D surface plot
plot_3d_surface()
