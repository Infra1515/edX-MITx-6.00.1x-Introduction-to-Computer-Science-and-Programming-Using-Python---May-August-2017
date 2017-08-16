def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        temp = 1
        for i in range(exp):
            s = temp
            s = temp * base
            temp = s
    return float(s)


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp-1)

def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    gcd = 0
    for i in range(1,b+1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) <= 1:
        return aStr == char
    else:
        middle = (len(aStr)-1)// 2
        if aStr[middle] == char:
            return True
        elif aStr[middle] < char:
            return isIn(char, aStr[middle+1:])
        else:
            return isIn(char, aStr[:middle])
