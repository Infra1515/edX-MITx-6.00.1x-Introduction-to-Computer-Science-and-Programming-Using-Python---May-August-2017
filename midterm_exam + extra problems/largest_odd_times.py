def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None
    """
    only_odd_numbers = []
    myDict = {}
    for element in L:
        if element in myDict:
            myDict[element] += 1
        else:
            myDict[element] = 1

    for key, value in myDict.items():
        if value % 2 != 0:
            only_odd_numbers.append(key)

    if len(only_odd_numbers) == 0:
        return None
    else:
        return max(only_odd_numbers)
