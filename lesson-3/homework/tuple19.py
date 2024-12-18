def remove_element_by_value(tup, element):
    if element in tup:
        index = tup.index(element)  # Find the index of the first occurrence
        return tup[:index] + tup[index+1:]  # Create a new tuple without the element
    return tup  # Return the original tuple if the element is not found