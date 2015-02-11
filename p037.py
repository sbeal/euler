# Steve Beal
# Project Euler problem 37 solution
# 2/10/15

# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and remain prime
# at each stage: 3797, 797, 97, and 7. Similarly, we can work from right to
# left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to
# right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from utils import prime_sieve, is_prime

def is_truncatable_prime(n):
    if n <= 7:
        return False

    right_to_left = n
    left_to_right = 0
    i = 0
    while right_to_left > 0:
        # this is like removing digits from right to left, since we divide
        # by 10 each time
        if not is_prime(right_to_left):
            return False

        # divide by 10, and capture the rightmost digit
        right_to_left, rem = divmod(right_to_left, 10)

        # now we can add the digit we captured by its original place-value
        # to build up the value we'd have if we were actually removing digits
        # from left to right
        left_to_right += rem * (10**i)
        if not is_prime(left_to_right):
            return False
        i += 1

    return True


def sum_eleven_truncatable_primes():
    truncatable_primes = set()
    # start the prime sieve with primes up to 4096 since we know 3797 works
    n = 12
    while len(truncatable_primes) < 11:
        # keep doubling the size of the prime sieve as needed to find the 11
        # truncatable primes
        primes = prime_sieve(2**n)
        for p in primes:
            if is_truncatable_prime(p):
                truncatable_primes.add(p)
        n += 1

    return sum(truncatable_primes)

print(sum_eleven_truncatable_primes())