# Steve Beal
# Project Euler problem 4 solution
# 1/31/14

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

from utils import is_palindrome

# add products only if they are palindromes, then get max
# much slower due to all the calls to is_palindrome
products = [i*j for i in range(999,99,-1) for j in range(i,99,-1) if is_palindrome(str(i*j))]
print max(products)


# get all products, then check if each is palindrome from biggest to smallest
# note: this method is much faster
products = sorted([i*j for i in range(999,99,-1) for j in range(i,99,-1)], reverse=True)
for i in range(len(products)-1):
	if is_palindrome(str(products[i])):
		print products[i]
		break

# and a bit more optimized
# even faster since we cut off many iterations
longest = 0
products = []
for i in range(999,99,-1):
	for j in range(i,99,-1):
		if i*j < longest:
			break
		if is_palindrome(str(i*j)):
			longest = i*j
print longest