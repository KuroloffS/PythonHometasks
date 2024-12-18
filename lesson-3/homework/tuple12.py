def second_largest(tup):
    unique_elements = set(tup)  # Remove duplicates
    if len(unique_elements) < 2:
        return None  # Return None if there are fewer than 2 unique elements
    unique_elements.remove(max(unique_elements))  # Remove the largest element
    return max(unique_elements)  # The new largest element is the second largest overall