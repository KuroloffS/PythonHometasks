def get_unique_elements(tup):
    seen = set()
    return tuple(element for element in tup if element not in seen and not seen.add(element))


