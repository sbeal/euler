# Steve Beal
# Project Euler problem 38 solution
# 3/7/15

# Take the number 192 and multiply it by each of 1, 2, and 3:
# 192 x 1 = 192
# 192 x 2 = 384
# 192 x 3 = 576

# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1, 2, 3).

# The same can be achieved by starting with 9 and multiplying by
# 1, 2, 3, 4, and 5, giving the pandigital 918273645, which is the concatenated
# product of 9 and (1, 2, 3, 4, 5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as
# the concatenated product of an integer with (1, 2, ..., n) where n > 1?

def largest_concat_product_pandigital():

    pan_set = set([str(d) for d in range(1, 10)])

    # we start at 9876 because it's the largest 4-digit number than can be part
    # of a pandigital. we want a 4-digit number since we are required to
    # multiply by at least (1, 2). if we chose anything more than 4 digits, we
    # would be guaranteeing a concatenated product of 10+ digits, which fails.
    x = 9876
    while x > 0:

        # as mentioned above, if we have a 4-digit number, multiplying by any
        # more than (1, 2) will give 12+ digits, which is too many, so our
        # upper bound is 2.
        if x >= 1000:
            n = 2

        # multiplying a 3-digit number by any more than (1..3) gives 12+
        # digits, which is too many, so our upper bound is 3
        elif x >= 100:
            n = 3
    
        # multiplying a 2-digit number by any more than (1..4) gives 10+
        # digits, which is too many, so our upper bound is 4
        elif x >= 10:
            n = 4
        
        # multiplying a 1-digit number by any more than (1..9) gives 10+
        # digits, which is too many, so our upper bound is 4
        elif x >= 1:
            n = 9
        else:
            n = 0

        # create a string of all the products, and concatenate them
        s_products = "".join([str(x * i) for i in range(1, n+1)])
        if len(s_products) == 9:
            if set(s_products) == pan_set:
                # this must be the largest since we started from the largest
                # substring of 987654321 possible. return early.
                return s_products
        x -= 1

    return None


print(largest_concat_product_pandigital())
