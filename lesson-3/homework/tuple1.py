def count_occurrences(tup, element):
    return tup.count(element)

# Example usage
my_tuple = (1, 2, 3, 2, 4, 2, 5)
element = 2
result = count_occurrences(my_tuple, element)
print(f"The element {element} appears {result} times in the tuple.")
