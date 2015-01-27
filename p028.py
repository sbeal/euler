# Steve Beal
# Project Euler problem 28 solution
# 1/12/15

# Starting with the number 1 and moving to the right in a clockwise direction
# a 5 by 5 spiral is formed as follows:
# *21* 22  23  24  *25*
# 20  *7*  8  *9*  10
# 19  6   *1*  2   11
# 18 *5*   4  *3*  12
# *17* 16  15 14  *13*

# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001
# spiral formed in the same way?



# These solutions are based on the observation that the length of a diagonal
# from center to corner is n//2 + 1 and,
# at each level of the spiral (level 0 = [1], level 1 = [3, 5, 7, 9], ...)
# each corner value increases by 2*(i+1) where i is the level

def spiral_sum_with_vals(n):
    diag_len = n//2 + 1
    num_corner_vals = 4*diag_len - 3
    corner_vals = [1]*num_corner_vals
    mult = 1
    for i in range(1, num_corner_vals):
        corner_vals[i] = corner_vals[i-1] + 2*mult
        if i % 4 == 0:
            mult += 1
        
    return sum(corner_vals), corner_vals

def spiral_sum_no_vals(n):
    diag_len = n//2 + 1
    num_corner_vals = 4*diag_len - 3
    prev = total = mult = 1
    for i in range(1, num_corner_vals):
        prev += 2*mult
        total += prev
        if i % 4 == 0:
            mult += 1
    return total

# input N is the dimension of the N x N grid
# print(spiral_sum_with_vals(1001))
print(spiral_sum_no_vals(1001))