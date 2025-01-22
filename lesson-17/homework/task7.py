import matplotlib.pyplot as plt

def plot_bar_chart():
    try:
        # Define product names and sales data
        products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
        sales = [200, 150, 250, 175, 225]

        # Define custom colors for the bars
        bar_colors = ['blue', 'green', 'red', 'purple', 'orange']

        # Create the bar chart
        plt.figure(figsize=(8, 6))
        plt.bar(products, sales, color=bar_colors, edgecolor='black')

        # Add title and axis labels
        plt.title("Sales Data for Different Products", fontsize=14)
        plt.xlabel("Products", fontsize=12)
        plt.ylabel("Sales (Units)", fontsize=12)

        # Show the chart
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to generate the bar chart
plot_bar_chart()
