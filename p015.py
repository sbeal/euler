# Steve Beal
# Project Euler problem 15 solution
# 2/11/14

# Starting in the top left corner of a 2x2 grid, and only being able to move 
# right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there in a 20x20 grid?

from utils import nCk, pascal_triangle

size = 20

# we need to make size steps down, and size steps right for a total of 2*size
# steps. nCk(size*2, size) counts the number of ways to choose which of the 
# 2*size steps are down (or right), which is also the number of lattice paths.
# for example, in a 2x2 grid, we could choose the down steps to be:
# 1 and 2, 1 and 3, 1 and 4, 2 and 3, 2 and 4, or 3 and 4, and since the right
# steps much be the remaining steps (i.e. there are no more options), this is
# the number of lattice paths
print nCk(size*2, size)


# we could also count the number of paths to each junctions, of which there 
# are (size+1)^2, which is the same as computing a subset of pascal's triangle.
# then we can grab the middle element in row 2*size of pascal's triangle
# where the first row is row 0. it must be a middle element to be a square grid

# get pascal's triangle up through row 2*size
pascal = pascal_triangle(2*size)
# get middle element, this works due to int division
pos = (len(pascal[2*size]) / 2)

print pascal[2*size][pos]