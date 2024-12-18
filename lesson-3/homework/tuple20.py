def create_nested_tuple(tup, group_size):
    if group_size <= 0:
        return ()  # Return an empty tuple for invalid group sizes
    return tuple(tup[i:i+group_size] for i in range(0, len(tup), group_size))

# Example usage
my_tuple = (1, 2, 3, 4, 5, 6, 7)
group_size = 2
result = create_nested_tuple(my_tuple, group_size)
print(f"The nested tuple is: {result}")
