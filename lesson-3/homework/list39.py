# Define the original list and the number of elements per sublist
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sublist_size = 3

# Create the nested list
nested_list = [my_list[i:i + sublist_size] for i in range(0, len(my_list), sublist_size)]

print(nested_list)
