# Steve Beal
# Project Euler problem 23 solution
# 2/22/14

# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of
# 28 would be 1+2+4+7+14=28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less
# than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By
# mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit
# cannot be reduced any further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of two abundant numbers
# is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.

from utils import sum_proper_divisors

def sum_non_abundant_sums():

    # get abundant numbers up to 28123 since everything greater than this
    # can be written as sums of abundant numbers
    abundant = set()
    total = 0
    for n in range(1, 28123):
        if sum_proper_divisors(n) > n:
            abundant.add(n)

        # check if any subtracting an abundant number yields another...if not,
        # this number is not representable as the sum of two abundant numbers
        if not any((n-a in abundant) for a in abundant):
            total += n
    return total

print(sum_non_abundant_sums())
