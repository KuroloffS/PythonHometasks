def check_element(tup, element):
    return element in tup

# Example usage
my_tuple = (1, 2, 3, 4, 5)
element = 3
result = check_element(my_tuple, element)
print(f"Element {element} is present in the tuple: {result}")
