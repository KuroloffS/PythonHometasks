def first_element(tup):
    if tup:
        return tup[0]
    else:
        return None  
my_tuple = (1, 2, 3, 4, 5)
empty_tuple = ()

print(f"The first element is: {first_element(my_tuple)}")
print(f"The first element in the empty tuple is: {first_element(empty_tuple)}")
