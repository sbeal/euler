# Steve Beal
# Project Euler problem 24 solution
# 2/23/14

# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
# 012 021 102 120 201 210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
# 5, 6, 7, 8 and 9?

def permutations(s):
    if len(s) <= 1:
        return [s]

    sub_perms = permutations(s[1:])
    first = s[0]
    perms = []
    for perm in sub_perms:
        for i in range(len(perm)+1):
            perms.append(perm[:i] + first + perm[i:])
    return perms

def nth_permutation_of_digits(n):
    perms = sorted(permutations("0123456789"))
    return perms[n-1]

print(nth_permutation_of_digits(1000000))