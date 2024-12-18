# Define the list and the rotation count
my_list = [1, 2, 3, 4, 5]
rotation_count = 2

# Perform the rotation
rotated_list = my_list[:]
for _ in range(rotation_count):
    rotated_list.insert(0, rotated_list.pop())

print(rotated_list)
