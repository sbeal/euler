# Steve Beal
# Project Euler problem 21 solution
# 2/15/14

# Let d(n) be defined as the sum of the proper divisors of n (the numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 7, and 142; so d(284) = 220.

# Evaluate the sum of all amicable numbers under 10000.

from utils import prime_factorize

# this uses the fact that the sum of divisors of n is equal to the product
# of the sum of each prime factor raised to 0,1,...,k
def d(n):
    total = 1
    for pair in prime_factorize(n):
        b,e = pair
        s = 0
        while e >= 0:
            s += b**e
            e -= 1
        total *= s
    return total - n

s = 0
amicables = set()
for a in range(2, 10000):
    if a in amicables:
        continue
    b = d(a)
    if d(b) == a and a != b:
        amicables.add(a)
        amicables.add(b)
        s = s + a + b

print s