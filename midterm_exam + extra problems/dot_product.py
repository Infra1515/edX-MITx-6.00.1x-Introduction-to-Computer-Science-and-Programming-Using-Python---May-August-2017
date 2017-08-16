def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    def dotProduct(listA,listB):
    counter = 0
    for i in range(len(listA)):
        counter += listA[i] * listB[i]

    return counter
