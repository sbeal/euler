# Steve Beal
# Project Euler problem 21 solution
# 2/15/14

# Let d(n) be defined as the sum of the proper divisors of n (the numbers
# less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair
# and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are
# 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 7, and 142; so d(284) = 220.

# Evaluate the sum of all amicable numbers under 10000.

from utils import sum_proper_divisors

def sum_amicables_under_n(n):
    amicables = set()
    for a in range(2, n):
        if not a in amicables:
            b = sum_proper_divisors(a)
            if sum_proper_divisors(b) == a and a != b:
                amicables.add(a)
                amicables.add(b)
    return sum(amicables)

print(sum_amicables_under_n(10000))