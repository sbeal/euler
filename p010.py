# Steve Beal
# Project Euler problem 10 solution
# 2/1/14

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from utils import prime_sieve

def sum_of_primes_under(n):
    return sum(prime_sieve(n))

print(sum_of_primes_under(2000000))