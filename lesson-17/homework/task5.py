import matplotlib.pyplot as plt
import numpy as np

def plot_histogram():
    try:
        # Generate random dataset of 1000 values from a normal distribution (mean=0, std=1)
        mean = 0
        std_dev = 1
        dataset = np.random.normal(mean, std_dev, 1000)

        # Plot the histogram
        plt.figure(figsize=(8, 6))
        plt.hist(dataset, bins=30, color='blue', alpha=0.7, edgecolor='black')

        # Add title and axis labels
        plt.title("Histogram of Random Dataset (Normal Distribution)", fontsize=14)
        plt.xlabel("Value", fontsize=12)
        plt.ylabel("Frequency", fontsize=12)

        # Show the plot
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to generate the histogram
plot_histogram()
