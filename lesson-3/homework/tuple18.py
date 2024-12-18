def min_of_subtuple(tup, start, end):
    if start < 0 or end > len(tup) or start >= end:
        return None  # Handle invalid ranges
    return min(tup[start:end])
