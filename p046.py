# Steve Beal
# Project Euler problem 46 solution
# 8/29/15

# It was propsed by Christian Golbach that every odd composite number can be
# written as the sum of a prime and twice a square.

# 9 = 7 + 2*1^2
# 15 = 7 + 2*2^2
# 21 = 3 + 2*3^2
# 25 = 7 + 2*3^2
# 27 = 19 + 2*2^2
# 33 = 31 + 2*1^2

from utils import is_prime
from utils import prime_sieve
from math import sqrt

def is_twice_a_square(n):
    # could "optimize" to check if n/2 is a whole number...might not be faster
    return sqrt(n/2) % 1.0 == 0

def is_goldbach(n):
    primes = prime_sieve(n)
    for p in reversed(primes):
        if is_twice_a_square(n-p):
            return True
    return False

def smallest_non_goldbach_odd_composite():
    x = 35 # we know it's at least this big
    while True:
        if not is_prime(x):
            if not is_goldbach(x):
                return x
        x += 2

if __name__ == '__main__':
    print(smallest_non_goldbach_odd_composite())