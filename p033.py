# Steve Beal
# Project Euler problem 33 solution
# 2/8/15

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician
# in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which
# is correct, is obtained by cancelling the 9s.

# We shall consider fractions like 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less
# than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.

from utils import gcd

def reduce_fraction(num, denom):
    old_num, old_denom = num, denom
    g = gcd(num, denom)
    num //= g
    denom //= g
    while num != old_num and denom != old_denom:
        old_num, old_denom = num, denom
        g = gcd(num, denom)
        num //= g
        denom //= g
    return (num, denom)

def digit_cancelling_fractions():

    non_trivial = []

    # Check all fractions from 10/11 to 98/99 for the digit-cancelling property
    for denom in range(11, 100):
        for num in range(10, denom):
            nd1 = num % 10
            nd10 = (num // 10) % 10
            dd1 = denom % 10
            dd10 = (denom // 10) % 10
            
            # Check that the ones digit in the numerator == the tens digit
            # in the denominator, and that the remaining ones digit in the
            # denominator is not 0. This avoids trivial fractions like
            # 11/22, 30/50, and also division by zero errors. We don't need to
            # check other cases where the numerator and denominator have the
            # same tens digit, like 11/12, because no such fraction could ever
            # be as small as 1/2, which is the largest fraction resulting from
            # the ones digits. A similar argument applies to fractions with the
            # same ones digit in the numerator and denominator like 11/21.

            if nd1 == dd10 and dd1 != 0:
                if nd10 / dd1 == num / denom:
                    non_trivial.append((num, denom))

    num = denom = 1
    for fraction in non_trivial:
        num *= fraction[0]
        denom *= fraction[1]
    reduced = reduce_fraction(num, denom)
    return reduced[1]

print(digit_cancelling_fractions())

