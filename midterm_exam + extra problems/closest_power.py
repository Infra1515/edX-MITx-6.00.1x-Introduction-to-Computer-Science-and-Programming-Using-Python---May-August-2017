def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    searched_exponent = 0
    # in order to avoid TypeError: float - convert num to float
    if type(num) == float:
        num = int(num)

    # store the results of base ** i in a dictionary in order to compare
    # not seperate exponent and result value
    # once the value gets bigger or equal to num - break the loop
    # values are stored a exponent : int
    results = {}
    counter = 0
    for i in range(0, num+1):
        if counter >= num:
            break
        counter = base **  i
        results[i] = counter
    # create a copy of results dict in order to avoid modifying it
    resultCopy = results.copy()
    # find the smallest difference between num and base ** exponent
    # and store it as dict[exponent] : num - results[base**exponent]
    for key, value in results.items():
        resultCopy[key] = abs(num - results[key])
    # initialize a counter variable in order to check if there are equal values
    i = 0
    # loop throuh key,value in a dict and find the key that has the minimal
    # difference between num - base**exp that we stored earlier
    # once found set the key ( which is the exponent) to searched_exponent
    for k, v in resultCopy.items():
        if v == min(resultCopy.values()):
            i += 1
            searched_exponent = k
    # if the value has occured in more then one key ie {0: 135, 1: 120, 2: 120}
    # return the exponent that is smaller
    if i != 1:
        searched_exponent -= 1

    return searched_exponent

print(closest_power(16,136.0))
