# Steve Beal
# Project Euler problem 27 solution
# 1/11/15

# Euler discovered the remarkable quadratic formula n^2 + n + 41

# It turns out that the formula will produce 40 primes for the consecutive
# values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is
# divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
# divisible by 41.

# The incredible formula n^2 - 79n + 1601 was discovered, which produces
# 80 primes for the consecutive values n = 0 to 79. The product of the
# coefficients, -79 and 1601, is -126479.

# Considering quadratics of the form n^2 + an + b, where |a|, |b| < 1000
# where |n| is the modulus/absolute value of n, e.g. |11| = 11 and |-4| = 4

# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n,
# starting with n = 0.

from utils import is_prime

def num_consecutive_primes(a, b):
    n = 0
    val = n**2 + a*n + b
    num_primes = 0
    while is_prime(val):
        num_primes += 1
        n += 1
        val = n**2 + a*n + b
    return num_primes

max_primes = -1
prod = 0
for a in range(-999, 1000):
    for b in range(-999, 1000):
        num_primes = num_consecutive_primes(a, b)
        if num_primes > max_primes:
            max_primes = num_primes
            prod = a*b


print max_primes, prod