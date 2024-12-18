def second_smallest(tup):
    unique_elements = set(tup)  # Remove duplicates
    if len(unique_elements) < 2:
        return None  # Return None if there are fewer than 2 unique elements
    unique_elements.remove(min(unique_elements))  
    return min(unique_elements)  