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
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms.
# Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million


from utils import collatz

def collatz_len(n, len_dict):
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

def start_of_longest_collatz_chain_under_n(limit):
    len_dict = {}
    collatz_lens = [collatz_len(x, len_dict) for x in range(limit)]
    max_len = max(collatz_lens)
    max_start = collatz_lens.index(max_len)
    return max_start

limit = 1000000
print(start_of_longest_collatz_chain_under_n(limit))
