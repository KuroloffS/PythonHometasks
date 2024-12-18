import random

# 1. Union of Sets
def union_of_sets(set1, set2):
    return set1.union(set2)

# 2. Intersection of Sets
def intersection_of_sets(set1, set2):
    return set1.intersection(set2)

# 3. Difference of Sets
def difference_of_sets(set1, set2):
    return set1.difference(set2)

# 4. Check Subset
def check_subset(set1, set2):
    return set1.issubset(set2)

# 5. Check Element
def check_element(set1, element):
    return element in set1

# 6. Set Length
def set_length(set1):
    return len(set1)

# 7. Convert List to Set
def convert_list_to_set(lst):
    return set(lst)

# 8. Remove Element
def remove_element(set1, element):
    set1.discard(element)  # discard won't raise an error if element doesn't exist
    return set1

# 9. Clear Set
def clear_set(set1):
    set1.clear()
    return set1

# 10. Check if Set is Empty
def check_if_empty(set1):
    return len(set1) == 0

# 11. Symmetric Difference
def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

# 12. Add Element
def add_element(set1, element):
    set1.add(element)
    return set1

# 13. Pop Element
def pop_element(set1):
    return set1.pop() if set1 else None

# 14. Find Maximum
def find_maximum(set1):
    return max(set1) if set1 else None

# 15. Find Minimum
def find_minimum(set1):
    return min(set1) if set1 else None

# 16. Filter Even Numbers
def filter_even_numbers(set1):
    return {num for num in set1 if num % 2 == 0}

# 17. Filter Odd Numbers
def filter_odd_numbers(set1):
    return {num for num in set1 if num % 2 != 0}

# 18. Create a Set of a Range
def create_set_of_range(start, end):
    return set(range(start, end+1))

# 19. Merge and Deduplicate
def merge_and_deduplicate(list1, list2):
    return set(list1 + list2)

# 20. Check Disjoint Sets
def check_disjoint_sets(set1, set2):
    return set1.isdisjoint(set2)

# 21. Remove Duplicates from a List
def remove_duplicates_from_list(lst):
    return list(set(lst))

# 22. Count Unique Elements
def count_unique_elements(lst):
    return len(set(lst))

# 23. Generate Random Set
def generate_random_set(size, range_start, range_end):
    return set(random.randint(range_start, range_end) for _ in range(size))

# Test cases
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
lst = [1, 2, 3, 4, 5, 1, 2, 3]

# Example test calls
print(union_of_sets(set1, set2))
print(intersection_of_sets(set1, set2))
print(difference_of_sets(set1, set2))
print(check_subset(set1, set2))
print(check_element(set1, 3))
print(set_length(set1))
print(convert_list_to_set(lst))
print(remove_element(set1, 3))
print(clear_set(set1))
print(check_if_empty(set1))
print(symmetric_difference(set1, set2))
print(add_element(set1, 7))
print(pop_element(set1))
print(find_maximum(set2))
print(find_minimum(set2))
print(filter_even_numbers(set2))
print(filter_odd_numbers(set2))
print(create_set_of_range(1, 5))
print(merge_and_deduplicate([1, 2, 3], [3, 4, 5]))
print(check_disjoint_sets(set1, set2))
print(remove_duplicates_from_list(lst))
print(count_unique_elements(lst))
print(generate_random_set(5, 1, 10))
