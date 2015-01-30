# Steve Beal
# Project Euler problem 67 solution
# 2/13/14

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23

# Find the maximum total from top to bottom in p67.txt, a 15K text file containing a triangle with a hundred rows.

# NOTE: this is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 2^99
# altogether! If you could check one trillion (10^12) routes every second it would take over twenty billion years to check them all. There is an
# efficient algorithm to solve it. ;o)


def max_triangle_total(triangle_rows):
    # go from bottom up and compute the max value reachable
    # from each position (and modify the rows matrix in place)
    for i in range(len(triangle_rows)-2, -1, -1):
        row = rows[i]
        row_below = rows[i+1]
        for j in range(len(row)):
            row[j] += max(row_below[j], row_below[j+1])

    return rows[0][0]

rows = []
with open("p067.txt", "r") as f:
    for line in f:
        stripped = line.strip()
        if stripped:
            rows.append([int(x) for x in stripped.split()])


print(max_triangle_total(rows))
