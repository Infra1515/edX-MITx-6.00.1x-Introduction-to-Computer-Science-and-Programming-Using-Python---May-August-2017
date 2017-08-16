def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
        If there are no digits in s it raises a ValueError exception.
        For example, sum_digits("a;35d4") returns 12."""
    if s.isalpha():
        raise ValueError
    else:
        counter = 0
        for element in s:
            if element.isdigit():
                element = int(element)
                counter += element
    return counter
