def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''
    l1 = [str(x) for x in L1]
    l2 = [str(x) for x in L2]
    if sorted(l1) != sorted(l2):
        return False
    elif L1 == [] and L2 ==[]:
        return (None, None, None)
    else:
        myDict = {}

        for element in L1:
            if element in myDict:
                myDict[element] += 1
            else:
                myDict[element] = 1


        most_common_element_count = max(myDict.values())
        most_common_element_name = None
        for key, value in myDict.items():
            if value == most_common_element_count:
                most_common_element_name = key

        ans = (most_common_element_name, most_common_element_count,type(most_common_element_name))
        return ans
