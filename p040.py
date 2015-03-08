# Steve Beal
# Project Euler problem 40 solution
# 3/8/15

# An irrational decimal fraction is created by concatenating the positive
# integers: 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.
# If d_n represents the nth digit of the fractional part, find the value of
# the following expression:
# d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000

def champernownes_constant_power_of_10_digits_2(power_bound):

    # set initial values to assume we've grabbed d_1 and d_10 already to
    # make the rest of the math easier

    n = 11              # the current value of n we're "adding" to the decimal
    num_digits = 13     # number of digits we've seen so far
    digits_per_n = 2    # number of digits we add with each value of n
    cur_power_10 = 100  # the next threshold we need to look for
    result = 1          # holds the running result product
    do_diff = True      # check whether we've passed the next threshold

    while num_digits <= power_bound + digits_per_n:
        # if we've hit a power of 10, our digits_per_n goes up. also add 1 to
        # the num_digits, because this n had one more digit than we were adding
        # before. we also need to bump up the power of 10. we note that we 
        # should check whether we've seen at least as many digits as the next
        # power of 10 we're on.
        if n == cur_power_10:
            cur_power_10 *= 10 # set next threshold
            num_digits += 1    # we haven't counted 1 digit of this n yet
                               # since we've hit a new threshold
            digits_per_n += 1  # each n until next threshold has 1 more digit
            do_diff = True     # start checking whether the number of digits
                               # seen has passed the new threshold

        if do_diff:
            diff = num_digits - cur_power_10

            # we've seen 0 or more digits beyond the next digit we needed.
            # go backward by dividing by 10 to find the digit we need.
            if diff >= 0:
                temp = n
                for i in range(diff):
                    temp //= 10
                result *= (temp % 10)

                # don't check this again until we've hit the next power of 10
                do_diff = False

        num_digits += digits_per_n
        n += 1

    return result

print(champernownes_constant_power_of_10_digits_2(1000000))
