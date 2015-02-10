# Steve Beal
# Project Euler problem 34 solution
# 2/8/15

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of
# their digits.
# Note: as 1! and 2! are not sums they are not included.

from math import factorial

def factorial_digits():
    digit_facts = [factorial(x) for x in range(10)]
    total = 0

    # 9! = 362880, which is 6 digits. By looking at the largest possible
    # 7-digit number, 9999999, we see that the sum of its factorial digits is
    # also 7 digits. The largest 8-digit number, 99999999 also has a 7-digit
    # sum of factorial digits, so we need not consider 8-digit numbers. Since
    # with 7-digit numbers we cannot get a higher sum of factorial digits than
    # 9!*7, this will be our upper bound.
    bound = digit_facts[9]*7
    for i in range(3, bound):
        fact_sum = 0
        n = i
        while n > 0:
            n, r = divmod(n, 10)
            fact_sum += factorial(r)
        if fact_sum == i:
            total += i
    return total
print(factorial_digits())
