# Steve Beal
# Project Euler problem 6 solution
# 2/1/14

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.

def sum_square_diff_1(n):
    # only creating the range once
    r = list(range(1, n+1))
    sum_squares = sum(x**2 for x in r)
    squared_sum = sum(r) **2
    return abs(sum_squares - squared_sum)

def sum_square_diff_2(n):
    # written as a one-liner (but creating range twice)
    return abs(sum(x**2 for x in range(1, n+1)) - 
               sum(range(1, n+1))**2)

limit = 100
print(sum_square_diff_1(limit))
print(sum_square_diff_2(limit))