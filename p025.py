# Steve Beal
# Project Euler problem 25 solution
# 2/23/14

# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1

# Hence the first 12 terms will be:
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

# The 12th term, F12, is the first to contain three digits.
# What is the first term in the Fibonacci sequence to contain 1000 digits?

from utils import fib_gen

def first_fib_with_n_digits(n):
    # generate one fib value at a time until length == n
    g = fib_gen()
    term = 1
    while len(str(next(g))) != n:
        term += 1
    return term

print(first_fib_with_n_digits(1000))