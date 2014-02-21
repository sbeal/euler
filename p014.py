# Steve Beal
# Project Euler problem 14 solution
# 2/11/14

# The following iterative sequence is defined for the set of positive integers:
# n = n/2 if n is even
# n = 3n + 1 if n is odd
#
# Using the rule above and starting with 13, we get the following sequence:
# 13, 40, 20, 10, 5, 16, 8, 4, 2, 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting
# numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million


from utils import collatz, is_prime, prime_sieve

limit = 1000000

len_dict = {}
max_len = max_start = 1

def collatz_len(n):
    if n > 1:
        length = 1
        c = n
        while c != 1:
            c = collatz(c)
            if c in len_dict:
                length += len_dict[c]
                break
            else:
                length += 1
        len_dict[n] = length
        return length
    elif n == 1:
        return 1
    else:
        return 0


collatz_lens = map(collatz_len, range(1, limit))
max_len = max(collatz_lens)
max_start = collatz_lens.index(max_len)

print max_start, max_len
