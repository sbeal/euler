# Steve Beal
# Project Euler problem 50 solution
# 9/6/15

# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13

# This is the longest sum of consecutive primes that adds to a prime below
# one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a
# prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most
# consecutive primes?

from utils import prime_sieve

def prime_with_longest_sum_sequence(limit):
    prime_list = prime_sieve(limit)
    prime_set = set(prime_list)
    num_primes = len(prime_list)

    # brute force
    longest_len = 1
    longest_prime = 2
    for i in range(num_primes):
        total = 0
        j = 0
        while total < limit and i+j < num_primes:
            total += prime_list[i+j]
            if total in prime_set:
                if j+1 > longest_len:
                    longest_len = j+1
                    longest_prime = total
            j += 1
    return longest_prime

if __name__ == '__main__':
    print(prime_with_longest_sum_sequence(1000000))