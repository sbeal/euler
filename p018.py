# Steve Beal
# Project Euler problem 18 solution
# 2/13/14

# By starting at the top of the triangle below and moving to adjacent numbers
# on the row below, the maximum total from top to bottom is 23.
# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23

# Find the maximum total from top to bottom of the triangle in p18.txt

# NOTE: as there are only 16384 routes, it is possible to solve this problem
# by trying every route. However, Problem 67, is the same challenge with a
# triangle containing one-hundred rows; it cannot be solved by brute force,
# and requires a clever method! ;o)

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
with open("p018.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line:
            rows.append([int(x) for x in line.split()])


print(max_triangle_total(rows))