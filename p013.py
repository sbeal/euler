# Steve Beal
# Project Euler problem 13 solution
# 2/4/14

# Work out the first 10 digits of the sum of the following one-hundred
# 50-digit numbers (numbers omitted, see p013.txt)

def first_n_digits_large_sum_1(num_digits, large_sum):
    return str(large_sum)[:num_digits]


# or to avoid converting the number to a string, take advantage of the fact
# that any 10-digit number > 999,999,999 and repeatedly divide by 10
def first_n_digits_large_sum_2(num_digits, large_sum):

    # calculate a limit of num_digits consecutive 9s
    limit = 0
    for _ in range(num_digits):
        limit = limit*10 + 9

    while large_sum > limit:
        large_sum //= 10
    return large_sum


lines = []
with open("p013.txt", "r") as f:
    lines = [int(line.strip()) for line in f]

X = sum(lines)

print(first_n_digits_large_sum_1(10, X))
print(first_n_digits_large_sum_2(10, X))