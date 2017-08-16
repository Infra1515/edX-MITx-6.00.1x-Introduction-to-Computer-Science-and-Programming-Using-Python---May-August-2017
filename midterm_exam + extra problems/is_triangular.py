def is_triangular(x):
    """
    k,a positive integer
    returns True if k is triangular and False if not
    """

    count = 0

    for i in range(1,x+1):
        count += i

        if count == x:
            return True
        elif count > x:
            break

    return False
