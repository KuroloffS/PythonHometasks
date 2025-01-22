import matplotlib.pyplot as plt
import numpy as np

def create_scatter_plot():
    try:
        # Set random seed for reproducibility
        np.random.seed(42)

        # Generate 100 random points in 2D space from uniform distribution (0 to 10)
        x_values = np.random.uniform(0, 10, 100)
        y_values = np.random.uniform(0, 10, 100)

        # Generate random colors and markers for points
        random_colors = np.random.rand(100)
        marker_types = ['o', 's', 'D', '^', 'v', 'p', '*', 'h']
        random_markers = np.random.choice(marker_types, size=100)

        # Create the scatter plot
        plt.figure(figsize=(8, 6))
        for x, y, color, marker in zip(x_values, y_values, random_colors, random_markers):
            plt.scatter(x, y, color=plt.cm.viridis(color), marker=marker)

        # Add title, axis labels, and grid
        plt.title("Scatter Plot of Random Points in 2D Space", fontsize=14)
        plt.xlabel("X-axis", fontsize=12)
        plt.ylabel("Y-axis", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)

        # Show the plot
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to generate the plot
create_scatter_plot()
