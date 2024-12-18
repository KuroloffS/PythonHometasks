def repeat_elements(tup, times):
    if times <= 0:
        return ()  # Return an empty tuple for non-positive repetitions
    return tuple(element for element in tup for _ in range(times))


