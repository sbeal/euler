# Steve Beal
# Project Euler problem 36 solution
# 2/10/15

# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in
# both base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include
# leading zeros.)

from utils import is_palindrome, is_numeric_palindrome

def sum_double_base_palindromes_below_n(n):
    total = 0
    for i in range(1, n):
        if is_numeric_palindrome(i):
            # Chop the '0b' off the front of the string
            binary = bin(i)[2:]
            if is_palindrome(binary):
                total += i
    return total

print(sum_double_base_palindromes_below_n(1000000))