def last_element(tup):
    if tup:
        return tup[-1]
    else:
        return None  # or you can return a custom message or value

# Example usage
my_tuple = (1, 2, 3, 4, 5)
empty_tuple = ()

print(f"The last element is: {last_element(my_tuple)}")
print(f"The last element in the empty tuple is: {last_element(empty_tuple)}")
