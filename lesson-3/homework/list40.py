# Define the original list
my_list = [1, 2, 2, 3, 4, 3, 5, 6, 4]

# Create a new list with unique elements while maintaining the order
unique_list = []
seen = set()

for element in my_list:
    if element not in seen:
        unique_list.append(element)
        seen.add(element)

print(unique_list)
