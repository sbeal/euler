# Steve Beal
# Project Euler problem 41 solution
# 3/9/15

# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
# also prime.

# What is the largest n-digit pandigital prime that exists?

from utils import prime_sieve

def is_pandigital(n):
    s = str(n)
    bound = len(s)
    digits = set([str(x) for x in range(1, bound+1)])
    return set(s) == digits

def largest_pandigital_prime():
    
    # We could brute force this and check all primes up to 987654321 for
    # the pandigital property, but this would be slow (especially in Python).
    # Instead, borrow the idea from elsewhere that if the sum of the digits in
    # a number is divisible by 3, the number is divisble by 3 (and not prime).
    # If we look at the digit sums of n-digit pandigital numbers with 
    # 1 <= n <= 9, we notice that only 4-digit and 7-digit pandigital numbers
    # are not divible by 3 and therefore might not be prime. So, let's check
    # all the primes up to 7654321 (largest 7-digit pandigital number).

    primes = prime_sieve(7654321)
    for i in range(len(primes)-1, -1, -1):
        if is_pandigital(primes[i]):
            return primes[i]
    return 0

print(largest_pandigital_prime())