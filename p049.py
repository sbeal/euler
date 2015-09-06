# Steve Beal
# Project Euler problem 49 solution
# 9/6/15

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
# increases by 3330, is unusual in two ways: (i) each of the three terms are
# prime, and, (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this
# sequence?

from utils import prime_sieve, unique_permutations, permutations
from collections import defaultdict

def three_term_arithmetic_sequence(num_list):

    if len(num_list) < 3:
        return []

    diffs = defaultdict(list)

    # find the diff for every pair
    for i in range(len(num_list)-1):
        a = int(num_list[i])
        for j in range(i+1, len(num_list)):
            b = int(num_list[j])
            if a < b:
                diff = b - a
                diffs[diff].append((a, b))
            else:
                diff = a - b
                diffs[diff].append((b, a))
            

    sequence = []

    # sort all in order of first element, then check if there's sequence
    for k, v in diffs.items():
        v = sorted(v, key=lambda pair: pair[0])
        if len(v) >= 2:
            for i in range(len(v)-1):
                for j in range(i+1, len(v)):
                    if v[i][1] == v[j][0]:
                        sequence.append(v[i][0])
                        sequence.append(v[i][1])
                        sequence.append(v[j][1])
    
    return sequence


def arithmetic_prime_permutations():
    four_digit_primes = set(str(x) for x in prime_sieve(9999) if x > 999)

    seq_strings = set()
    for p in four_digit_primes:
        odd_prime_perms = [u for u in unique_permutations(p) if u in four_digit_primes]
        seq = three_term_arithmetic_sequence(odd_prime_perms)
        if seq:
            seq_string = "".join(str(x) for x in seq)
            seq_strings.add(seq_string)
    return seq_strings


if __name__ == '__main__':
    for p in arithmetic_prime_permutations():
        print(p)


