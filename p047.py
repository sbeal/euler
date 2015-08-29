# Steve Beal
# Project Euler problem 47 solution
# 8/29/15

# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 x 7
# 15 = 3 x 5

# The first three consecutive numbers to have have three distince prime factors
# are:
# 644 = 2^2 x 7 x 23
# 645 = 3 x 5 x 43
# 646 = 2 x 17 x 19

# Find the first four consecutive integers to have four distinct prime factors.
# What is the first of these numbers?

from utils import prime_factorize

def first_four_consecutive_with_four_distinct_prime_factors():
    consecs = []
    x = 647
    seen_factors = set()
    while len(consecs) < 4:
        factors = prime_factorize(x)
        # need at least 4 prime factors, otherwise try next val
        if len(factors) != 4:
            consecs = []
            seen_factors = set()
        else:
            for f in factors:
                # need all distinct factors, otherwise try next val
                if f not in seen_factors:
                    seen_factors.add(f)
                else:
                    consecs = []
                    seen_factors = set()
                    break
            # check whether we broke the loop, or finished successfully
            if len(seen_factors) > 0:
                consecs.append(x)
        x += 1

    return consecs





if __name__ == '__main__':
    print(first_four_consecutive_with_four_distinct_prime_factors())