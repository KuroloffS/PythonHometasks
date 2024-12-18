# Define the list
main_list = [1, 3, 5, 2, 8, 6, 4]

# Specify the range of the sublist
start_index = 2  # inclusive
end_index = 6    # exclusive

# Extract the sublist
sublist = main_list[start_index:end_index]

# Find the maximum element in the sublist
max_element = max(sublist)

print(f"The sublist is: {sublist}")
print(f"The maximum element in the sublist is: {max_element}")
