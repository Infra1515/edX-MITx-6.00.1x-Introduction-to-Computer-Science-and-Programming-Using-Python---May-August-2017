def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here

    l = []
    for elem in aDict:
        i = 0
        for item in aDict[elem]:
            if len(elem) > 0:
                i = i +1
                l.append(i)
    return len(l)


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    values = aDict.values()
    best = max(values)
    result = []
    for k in aDict:
        if aDict[k] == best:
            result.append(k)
    return result[0]
