# Steve Beal
# Project Euler problem 35 solution
# 2/10/15

# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 31, 37, 71, 73,
# 79 and 97.
# How many circular primes are there below one million?

from utils import prime_sieve, is_prime

def rotations(n):
    rotations = []
    s = str(n)
    for i in range(1, len(s)):
        rotations.append(int(s[i:] + s[:i]))
    return rotations


def num_circular_primes_below_n(n):
    count = 0
    for p in prime_sieve(n):
        all_prime = True
        for r in rotations(p):
            if not is_prime(r):
                all_prime = False
                break
        if all_prime:
            count += 1
    return count

print(num_circular_primes_below_n(1000000))
