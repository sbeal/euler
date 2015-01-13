# Steve Beal
# Project Euler problem 7 solution
# 2/1/14

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
# What is the 10001st prime number?

from utils import prime_sieve

def nth_prime(N):
    i = 0
    primes = []

    # increase size of the prime sieve until we have >= N prime
    while len(primes) < N:
        primes = prime_sieve(N*(2**i))
        i += 1
    return (primes[N-1], i)

print(nth_prime(1059))