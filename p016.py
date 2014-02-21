# Steve Beal
# Project Euler problem 16 solution
# 2/11/14

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

val = 2**1000

# "easy" way using string conversion
print sum(int(c) for c in str(val))

# another way by grabbing digits via modulus (slower if string is long)
s = 0
while val > 0:
    val, r = divmod(val, 10)
    s += r
print s