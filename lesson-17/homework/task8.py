import matplotlib.pyplot as plt
import numpy as np

def plot_stacked_bar_chart():
    try:
        # Define time periods and categories
        time_periods = ['T1', 'T2', 'T3', 'T4']
        categories = ['Category A', 'Category B', 'Category C']

        # Sample data for each category at each time period
        data_category_a = [10, 15, 20, 25]
        data_category_b = [20, 25, 30, 35]
        data_category_c = [30, 35, 40, 45]

        # Convert time periods to a numpy array for bar positions
        x = np.arange(len(time_periods))

        # Plot the stacked bar chart
        plt.figure(figsize=(8, 6))
        plt.bar(x, data_category_a, label='Category A', color='blue')
        plt.bar(x, data_category_b, bottom=data_category_a, label='Category B', color='green')
        plt.bar(x, data_category_c, bottom=np.array(data_category_a) + np.array(data_category_b), label='Category C', color='orange')

        # Customize the chart
        plt.title("Stacked Bar Chart of Categories Over Time", fontsize=14)
        plt.xlabel("Time Periods", fontsize=12)
        plt.ylabel("Values", fontsize=12)
        plt.xticks(x, time_periods)
        plt.legend(title="Categories")

        # Show the chart
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to generate the stacked bar chart
plot_stacked_bar_chart()
