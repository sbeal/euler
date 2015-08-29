# Steve Beal
# Project Euler problem 48 solution
# 8/29/15

# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

# Note that instead of actually adding all these, we can get the last 10 digits
# of each, and add those.

def self_powers(last_power, num_digits):
    # this gives us a way to mask off the last 10 digits of a number
    mod_factor = 10**num_digits

    last_digits_total = 0

    for i in range(1, last_power+1):
        
        # rather than calculate the full power, keep calculating the last
        # num_digits digits
        prod = 1
        for j in range(i):
            prod = (prod * i) % mod_factor

        # instead of keeping full total, keep last num_digits digts
        last_digits_total = (last_digits_total + prod) % mod_factor
        print(last_digits_total)

    # this could theoretically happen if 0 is a leading digit
    last_digits_total = str(last_digits_total)
    while len(last_digits_total) < num_digits:
        last_digits_total = '0' + last_digits_total

    return last_digits_total

if __name__ == '__main__':
    print(self_powers(1000, 10))