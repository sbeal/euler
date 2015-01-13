# Steve Beal
# Project Euler problem 4 solution
# 1/31/14

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

from utils import is_palindrome, is_numeric_palindrome

def largest_palindrome_1():
    # add products only if they are palindromes, then get max
    # fairly slow due to all the calls to is_palindrome, and string conversions
    products = [i*j for i in range(999,99,-1)
                    for j in range(i,99,-1)
                    if is_palindrome(str(i*j))]
    return max(products)


def largest_palindrome_2():
    # get all products, then check if each is palindrome from big to small
    # faster than above by cutting off iterations, but slow string conversions
    products = sorted([i*j for i in range(999,99,-1) for j in range(i,99,-1)],
                      reverse=True)
    for i in range(len(products)-1):
        if is_palindrome(str(products[i])):
            return products[i]

def largest_palindrome_3():
    # a bit faster by not sorting, and cutting off some iterations
    # when we can't achieve a larger product in the inner loop
    longest = 0
    for i in range(999,99,-1):
        for j in range(i,99,-1):
            n = i*j
            if n < longest:
                break
            if is_palindrome(str(n)):
                longest = n
    return longest

def largest_palindrome_4():
    # and perhaps the fastest, since we use a numeric palindrome checking
    # function and avoid converting ints to strings
    longest = 0
    for i in range(999,99,-1):
        for j in range(i,99,-1):
            n = i*j
            if n < longest:
                break
            if is_numeric_palindrome(n):
                longest = n
    return longest

print(largest_palindrome_1())
print(largest_palindrome_2())
print(largest_palindrome_3())
print(largest_palindrome_4())
