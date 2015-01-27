# Steve Beal
# Project Euler problem 3 solution
# 1/31/14

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from utils import prime_factorize

def largest_prime_factor(n):
    
    factors = prime_factorize(n)

    # automatically maximizes on the first item in the tuple (take care here)
    return max(factors)[0]

val = 600851475143
print(largest_prime_factor(val))