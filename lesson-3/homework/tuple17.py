def max_of_subtuple(tup, start, end):
    if start < 0 or end > len(tup) or start >= end:
        return None  
    return max(tup[start:end])
