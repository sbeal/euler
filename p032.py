# Steve Beal
# Project Euler problem 32 solution
# 2/7/15

# We shall say that an n-digit number is pandigital if it makes use of all
# the digits 1 to n exactly once; for example, the 5-digit number, 15234, is
# 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39*186 = 7254, containing
# multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.

# Hint: Some products can be obtained in more than one way so be sure to only
# include it once in your sum.

DIGIT_SET = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

def is_pandigital(x, y, z):
    digits_seen = set()
    s = str(x) + str(y) + str(z)

    if len(s) > 9:
        return False

    for c in s:
        if not c.isdigit() or c in digits_seen:
            return False
        digits_seen.add(c)
    
    return digits_seen == DIGIT_SET


def pandigital_products():
    valid_products = set()

    # If the multiplicand has one digit, we must consider only 4-digit
    # multipliers, since any 1-digit * 4-digit product has >= 4 digits for a 
    # total of 9
    for i in range(1, 10):
        for j in range(1000, 10000):
            p = i*j
            if is_pandigital(i, j, p):
                valid_products.add(p)
    
    # If the multiplicand has two digits, we must consider only 3-digit
    # multipliers, since any 2-digit * 3-digit product has >= 5 digits for a
    # total of >= 9
    for i in range(10, 100):
        for j in range(100, 1000):
            p = i*j
            if is_pandigital(i, j, p):
                valid_products.add(p)

    # We could optimize the above loops a bit more to not generate some
    # values that we know will be too big, but it's not needed now
    
    return sum(valid_products)


print(pandigital_products())
