def gcd(x, y):

    # Compute the greatest common divisor
    if x%y == 0:
        return y
    else:
        return gcd(y, x%y)

def hasSamePrimeDivisors(x, y):
    gcd_value = gcd(x, y)   # The gcd contains all
                            # the common prime divisors
    while x != 1:

        x_gcd = gcd(x, gcd_value)
        if x_gcd == 1:
            # x does not contain any more 
            # common prime divisors
            break
        x /= x_gcd
    if x != 1:
        # If x and y have exactly the same common 
        # prime divisors, x must be composed by
        # the prime divisors in gcd_value. So
        # after previous loop, x must be one.
        return False
    while y != 1:
        y_gcd = gcd(y, gcd_value)
        if y_gcd == 1:
            # y does not contain any more
            # common prime divisors
            break
        y /= y_gcd
    return y == 1
    
def solution(A, B):
    count = 0
    for x,y in zip(A,B):
        if hasSamePrimeDivisors(x,y):
            count += 1
    return count