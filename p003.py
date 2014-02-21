# Steve Beal
# Project Euler problem 3 solution
# 1/31/14

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from utils import prime_factorize

val = 600851475143
# val = 13195

# get the prime factorization
factors = prime_factorize(val)

# automatically maximizes on the first item in the tuple (take care here)
print max(factors)[0]