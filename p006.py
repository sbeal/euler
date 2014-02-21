# Steve Beal
# Project Euler problem 6 solution
# 2/1/14

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

limit = 100


# only creating the range once
r = range(1, limit+1)
sum_squares = sum(map(lambda x:x**2, r))
squared_sum = sum(r) **2
print abs(sum_squares - squared_sum)


# written as a one-liner (but creating range twice)
print abs(sum(x**2 for x in range(1, limit + 1)) - sum(range(1, limit + 1))**2)