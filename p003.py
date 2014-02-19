# Steve Beal
# Project Euler problem 3 solution
# 1/31/14

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt
from utils import is_probably_prime, is_prime

val = 600851475143
# val = 13195

# method of continually reducing possible factors
# first get all odd factors not multiples of 3 or 5
possible_prime_factors = {x:True for x in range(3,int(sqrt(val))+1,2) if not (x > 5 and (x % 3 == 0 or x % 5 == 0))}

# then take out ones that aren't prime or aren't factors
for x in possible_prime_factors:
	if not is_probably_prime(x):
		possible_prime_factors[x] = False
	q, r = divmod(val, x)
	if not r == 0:
		possible_prime_factors[x] = False
# at the end, all we have is prime factors, so get the biggest
print max([x for x in possible_prime_factors.keys() if possible_prime_factors[x]])


# method of smartly adding factors
# note: only got this after reading answer
n = val
lpf = 1
if n % 2 == 0:
	lpf = 2
	while n % 2 == 0:
		n = n/2

f = 3
while n > 1:
	if n % f == 0:
		n = n/f
		lpf = f
		while n % f == 0:
			n = n/f
	f += 2
if n == 1:
	print lpf
else:
	print val