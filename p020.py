# Steve Beal
# Project Euler problem 20 solution
# 2/15/14

# n! means n * (n-1) * ... * 3 * 2 * 1
# For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
# and the sum of the digits in the number 10! is 3+6+2+8+8+0+0 = 27.
# Find the sum of the digits in the number 100!


from math import factorial


# easy way with converting to string
def sum_factorial_digits_1(n):
    fac = factorial(n)
    return sum(int(c) for c in str(fac))


# another way by grabbing digits via modulus (slower if string is very long)
def sum_factorial_digits_2(n):
    fac = factorial(n)
    total = 0
    while fac > 0:
        fac, r = divmod(fac, 10)
        total += r
    return total


n = 100

print(sum_factorial_digits_1(n))
print(sum_factorial_digits_2(n))