def f_add(a,b):
    return a + b
def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    # then dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})

    # transform both dicts items to a list of tuples
    lis = sorted(list(d1.items()) + list(d2.items()))
    d_1 = {}
    d_2 = {}
    # create the dict with keys that are in both dicts and pass their values
    # to f()
    for i in range(len(lis)-1):

        if lis[i][0] == lis[i+1][0]:
            d_1[lis[i][0]] = f(lis[i][1], lis[i+1][1])
    # create the dict with the keys that are unique for each dict
    for i in range(len(lis)):
        if lis[i][0] not in d_1.keys():
            d_2[lis[i][0]] = lis[i][1]



    result = (d_1,d_2)
    return result


print(dict_interdiff({4: 4, 5: 3, 6: 3, 8: 4, 9: 1, 10: 0}, {1: 1, 2: 2, 3: 3, 4: 5}))
