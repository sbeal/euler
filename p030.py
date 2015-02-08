# Steve Beal
# Project Euler problem 30 solution
# 1/27/15

# Surprisingly there are only three numbers that can be written as the sum of
# fourth powers of their digits:
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4

# As 1 = 1^4 is not a sum it is not included.
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the sum of fifth
# powers of their digits.

def digit_fifth_powers_sum():

    # To set upper bound, consider an n-digit number X whose digits we are
    # raising to the 5th power. If n is greater than the number of digits in
    # the maximum possible 5th power digit sum for an n-digit number, we need
    # not consider any numbers larger than X. We will start by looking
    # at 5-digit numbers since 9^5 = 59049. The greatest 5-digit number 99999
    # gives 5th power digit sum 295245, so we know all 5 digit numbers are
    # possible. The greatest 6-digit number 999999 gives 5th power digit sum
    # 354294. The greatest 7-digit number 9999999 gives 5th power digit sum
    # 413343, which is only 6 digits. So, we need not consider any 7-digit
    # numbers at all. Further, for 6 digits, we can only possibly get 5th power
    # digits sums up to 354294, so we need not consider any greater numbers.
    total = 0
    for num in range(2, 354295):
        digits_fifth_sum = sum(int(d)**5 for d in str(num))
        if num == digits_fifth_sum:
            total += num

    return total

print(digit_fifth_powers_sum())