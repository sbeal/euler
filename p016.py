# Steve Beal
# Project Euler problem 16 solution
# 2/11/14

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?


# "easy" way using string conversion
def sum_digits_1(n):
    return sum(int(c) for c in str(n))

# another way by grabbing digits via modulus
def sum_digits_2(n):
    total = 0
    while n > 0:
        n, r = divmod(n, 10)
        total += r
    return total


val = 2**1000

print(sum_digits_1(val))
print(sum_digits_2(val))
