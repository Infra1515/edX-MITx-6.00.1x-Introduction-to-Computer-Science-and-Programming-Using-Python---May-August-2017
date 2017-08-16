def flatten_list(t):
    """ Helper function that flattens a list """
    new_list = []
    for element in t:
        if isinstance(element,(list,tuple)):
            new_list.extend(flatten_list(element))
        else:
            new_list.append(element)
    return new_list

def max_val(t):
    """ t, tuple or list
    Each element of t is either an int, a tuple, or a list
    No tuple or list is empty
    Returns the maximum int in t or (recursively) in an element of t
    Example : max_val((5, (1,2), [[1],[2]])) returns 5.
    max_val((5, (1,2), [[1],[9]])) returns 9."""
    return max(flatten_list(t))
