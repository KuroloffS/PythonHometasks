def create_range_tuple(start, end):
    return tuple(range(start, end + 1))  # Include the end value

# Example usage
start = 1
end = 10
result = create_range_tuple(start, end)
print(f"The range tuple is: {result}")
