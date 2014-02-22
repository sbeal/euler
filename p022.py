# Steve Beal
# Project Euler problem 22 solution
# 2/22/14

# Using p022.txt, a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the
# alphabetical value for each name, multiply this value by its alphabetical
# position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which
# is 3+15+12+9+14=53, is the 938th name in the list. So COLIN would obtain a
# score of 938*53=49714.

# What is the total of all the name scores in the file?

import string

# get names into list and format, sort
names = []
with open("p022.txt") as f:
    names = f.readline().split(",")
names = [x.strip('"') for x in names]
names.sort()

# lookup table for values (A=1, B=2, ..., Z=26)
alpha_vals = dict(zip(string.uppercase, range(1,27)))

total = 0
for pos, name in enumerate(names):
    score = 0
    for char in name:
        score += alpha_vals[char]
    score *= (pos+1)
    total += score
print total