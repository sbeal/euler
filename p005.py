# Steve Beal
# Project Euler problem 5 solution
# 2/1/14

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from utils import lcm

def lcm_up_to(n):
	return lcm(1,range(2,n))

print lcm_up_to(20)