# Define the list and the target element
my_list = [1, 2, 3, 2, 4, 2, 5]
target = 2

# Find all indices using a for loop
indices = []
for index, value in enumerate(my_list):
    if value == target:
        indices.append(index)

print(indices)
