# Steve Beal
# Project Euler problem 16 solution
# 2/11/14

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

# easy way using string conversion

val = 2**1000
print sum(int(c) for c in str(val))