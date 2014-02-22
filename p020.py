# Steve Beal
# Project Euler problem 20 solution
# 2/15/14

# n! means n * (n-1) * ... * 3 * 2 * 1
# For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
# and the sum of the digits in the number 10! is 3+6+2+8+8+0+0 = 27.
# Find the sum of the digits in the number 100!


from math import factorial

n = 100
res = factorial(n)

# easy way with converting to string
print sum(int(c) for c in str(res))


# another way by grabbing digits via modulus (slower if string is very long)
s = 0
while res > 0:
    res, r = divmod(res, 10)
    s += r
print s