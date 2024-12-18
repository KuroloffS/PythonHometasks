# 1. Get Value
def get_value(dictionary, key, default=None):
    return dictionary.get(key, default)

# 2. Check Key
def check_key(dictionary, key):
    return key in dictionary

# 3. Count Keys
def count_keys(dictionary):
    return len(dictionary)

# 4. Get All Keys
def get_all_keys(dictionary):
    return list(dictionary.keys())

# 5. Get All Values
def get_all_values(dictionary):
    return list(dictionary.values())

# 6. Merge Dictionaries
def merge_dictionaries(dict1, dict2):
    result = dict1.copy()  # Start with the first dictionary
    result.update(dict2)  # Update with the second dictionary
    return result

# 7. Remove Key
def remove_key(dictionary, key):
    dictionary.pop(key, None)  # Remove the key if exists, else do nothing
    return dictionary

# 8. Clear Dictionary
def clear_dictionary():
    return {}

# 9. Check if Dictionary is Empty
def check_if_empty(dictionary):
    return len(dictionary) == 0

# 10. Get Key-Value Pair
def get_key_value_pair(dictionary, key):
    if key in dictionary:
        return (key, dictionary[key])
    return None

# 11. Update Value
def update_value(dictionary, key, new_value):
    if key in dictionary:
        dictionary[key] = new_value
    return dictionary

# 12. Count Value Occurrences
def count_value_occurrences(dictionary, value):
    return list(dictionary.values()).count(value)

# 13. Invert Dictionary
def invert_dictionary(dictionary):
    return {v: k for k, v in dictionary.items()}

# 14. Find Keys with Value
def find_keys_with_value(dictionary, value):
    return [k for k, v in dictionary.items() if v == value]

# 15. Create a Dictionary from Lists
def create_dict_from_lists(keys, values):
    return dict(zip(keys, values))

# 16. Check for Nested Dictionaries
def check_for_nested_dicts(dictionary):
    return any(isinstance(v, dict) for v in dictionary.values())

# 17. Get Nested Value
def get_nested_value(dictionary, outer_key, inner_key):
    outer_dict = dictionary.get(outer_key)
    if isinstance(outer_dict, dict):
        return outer_dict.get(inner_key)
    return None

# 18. Create Default Dictionary
def create_default_dict(default_value):
    return lambda: default_value

# 19. Count Unique Values
def count_unique_values(dictionary):
    return len(set(dictionary.values()))

# 20. Sort Dictionary by Key
def sort_dict_by_key(dictionary):
    return dict(sorted(dictionary.items()))

# 21. Sort Dictionary by Value
def sort_dict_by_value(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1]))

# 22. Filter by Value
def filter_by_value(dictionary, condition):
    return {k: v for k, v in dictionary.items() if condition(v)}

# 23. Check for Common Keys
def check_for_common_keys(dict1, dict2):
    return bool(set(dict1.keys()) & set(dict2.keys()))

# 24. Create Dictionary from Tuple
def create_dict_from_tuple(tup):
    return dict(tup)

# 25. Get the First Key-Value Pair
def get_first_key_value_pair(dictionary):
    if dictionary:
        first_key = next(iter(dictionary))
        return (first_key, dictionary[first_key])
    return None

# Example test cases
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'd': 5}
keys = ['a', 'b', 'c']
values = [1, 2, 3]

# Example test calls
print(get_value(dict1, 'b'))  # 2
print(check_key(dict1, 'b'))  # True
print(count_keys(dict1))  # 3
print(get_all_keys(dict1))  # ['a', 'b', 'c']
print(get_all_values(dict1))  # [1, 2, 3]
print(merge_dictionaries(dict1, dict2))  # {'a': 1, 'b': 4, 'c': 3, 'd': 5}
print(remove_key(dict1, 'b'))  # {'a': 1, 'c': 3}
print(clear_dictionary())  # {}
print(check_if_empty(dict1))  # False
print(get_key_value_pair(dict1, 'b'))  # ('b', 2)
print(update_value(dict1, 'b', 10))  # {'a': 1, 'b': 10, 'c': 3}
print(count_value_occurrences(dict1, 2))  # 1
print(invert_dictionary(dict1))  # {1: 'a', 2: 'b', 3: 'c'}
print(find_keys_with_value(dict1, 3))  # ['c']
print(create_dict_from_lists(keys, values))  # {'a': 1, 'b': 2, 'c': 3}
print(check_for_nested_dicts({'a': 1, 'b': {'x': 10}}))  # True
print(get_nested_value({'a': {'b': 2}}, 'a', 'b'))  # 2
print(create_default_dict(0)())  # 0
print(count_unique_values(dict1))  # 3
print(sort_dict_by_key(dict1))  # {'a': 1, 'b': 2, 'c': 3}
print(sort_dict_by_value(dict1))  # {'a': 1, 'b': 2, 'c': 3}
print(filter_by_value(dict1, lambda v: v % 2 == 0))  # {'b': 2}
print(check_for_common_keys(dict1, dict2))  # True
print(create_dict_from_tuple([('a', 1), ('b', 2)]))  # {'a': 1, 'b': 2}
print(get_first_key_value_pair(dict1))  # ('a', 1)
