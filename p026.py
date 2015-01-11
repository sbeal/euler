# Steve Beal
# Project Euler problem 26 solution
# 1/11/15

# A unit fraction contains 1 in the numerator. The decimal representation
# of the unit fractions with denominators 2 to 10 are given:
# 1/2 = 0.5
# 1/3 = 0.(3)
# 1/4 = 0.25
# 1/5 = 0.2
# 1/6 = 0.1(6)
# 1/7 = 0.(142857)
# 1/8 = 0.125
# 1/9 = 0.(1)
# 1/10 = 0.1

# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
# It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring
# cycle in its decimal fraction part.

def get_cycle_len(n):
    remainders = { 1: 0 }
    cycle_len = 0
    i, r, cycle_len = 0, 1, 0
    while True:
        # the next remainder is 10 times the previous one, mod divisor
        r = 10*r % n

        # if remainder is 0, we've divided evenly and don't have a cycle
        if r == 0:
            cycle_len = 0
            break
        else:
            # if we've seen this before, it's the end of the cycle
            if r in remainders:
                cycle_len = i + 1 - remainders[r]
                break
            # otherwise, the cycle continues
            else:
                remainders[r] = i + 1
        i+=1
    return cycle_len

def longest_reciprocal_cycle(d):
    # start from the bigger end, since it's more likely to have long cycles
    max_cycle_len = 0
    max_cycle_num = 1001
    for num in range(d, 1, -1):
        # max cycle len is num-1, so stop if it's already bigger than any of the
        # remaining numbers
        if max_cycle_len > num:
            break

        cycle = get_cycle_len(num)
        if cycle > max_cycle_len:
            max_cycle_len = cycle
            max_cycle_num = num

    return (max_cycle_num, max_cycle_len)


print longest_reciprocal_cycle(1000)
