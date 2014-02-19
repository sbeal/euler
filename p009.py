# Steve Beal
# Project Euler problem 9 solution
# 2/1/14

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
# For example 3^2 + 4^2 = 9 + 16 = 25 = 5^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc

total = 1000

# naive way
for a in range((total-3) / 3):
	for b in range(a+1, (total-a-1) / 2):
		c = total - a - b
		if a*a + b*b == c*c:
			print a*b*c



# slightly better way, using the knowledge that a = m^2-n^2, b = 2mn, c = m^2+n^2
# and that the upper limit for loops is total/6 since b=2mn and b < total/3
# gives us total/6 > mn, so at most m or n can be total/6 
m = 2
n = 1
for n in range(1, total/6):
	for m in range(n+1, total/6+1):
		a = m*m - n*n
		b = 2*m*n
		c = m*m + n*n
		if a+b+c == total:
			print a*b*c