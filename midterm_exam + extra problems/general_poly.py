def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
    def poly(num):
        k = len(L)-1
        result = 0
        summ = 0
        for i in range(len(L)):
            result = L[i] * num ** k
            summ += result
            k -= 1
        return summ
    return poly
