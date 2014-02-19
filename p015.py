# Steve Beal
# Project Euler problem 15 solution
# 2/11/14

# Starting in the top left corner of a 2x2 grid, and only being able to move 
# right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there in a 20x20 grid?

from utils import nCk, pascal_triangle

size = 20

# mathematically, but boring
print nCk(size*2, size)


# more intuitively, we could count the number of paths
# to each spot, of which there are (size+1)^2,
# which is the same as computing a subset of pascal's triangle
# then we can grab the middle element in row 2*size of pascal's triangle
# where the first row is row 0. it must be a middle element to be a square grid

# get pascal's triangle up through row 2*size
pascal = pascal_triangle(2*size)
# get middle element, this works due to int division
pos = (len(pascal[2*size]) / 2)

print pascal[2*size][pos]