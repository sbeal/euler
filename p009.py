# Steve Beal
# Project Euler problem 9 solution
# 2/1/14

# A Pythagorean triplet is a set of three natural numbers,
# a < b < c, for which, a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc

# naive way. return 0 if it doesn't exist
def pythagorean_triplet_product_1(n):
    for a in range((n-3) // 3):
        for b in range(a+1, (n-a-1) // 2):
            c = n - a - b
            if a*a + b*b == c*c:
                return a*b*c
    return 0


# better way using a = j^2-i^2, b = 2ji, c = j^2+i^2 (Euclid's formula)
# and that the upper limit for loops is n/6 since b=2ji and b < n/3
# gives us n/6 > ji, so at most j or i can be N/6 
def pythagorean_triplet_product_2(n):
    for i in range(1, n // 6):
        for j in range(i+1, (n // 6) + 1):
            a = j*j - i*i
            b = 2*j*i
            c = j*j + i*i
            if a+b+c == n:
                return a*b*c
    return 0


total = 1000
print(pythagorean_triplet_product_1(total))
print(pythagorean_triplet_product_2(total))