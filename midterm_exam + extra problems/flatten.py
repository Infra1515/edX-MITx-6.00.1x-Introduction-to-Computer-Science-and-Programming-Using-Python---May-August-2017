def flatten_recur(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''


    flatten_list = []
    for item in aList:
        if type(item) == list:
            flatten_list.extend(flatten(item))
        else:
            flatten_list.append(item)
    return flatten_list

def flatten_iter(l, ltypes=(list, tuple)):
    ltype = type(l)
    l = list(l)
    i = 0
    while i < len(l):
        while isinstance(l[i], ltypes):
            if not l[i]:
                l.pop(i)
                i -= 1
                break
            else:
                l[i:i + 1] = l[i]
        i += 1
    return ltype(l)

Z = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten_iter(Z))

# http://rightfootin.blogspot.bg/2006/09/more-on-python-flatten.html
