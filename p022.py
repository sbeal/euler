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

def alpha_val(c):
    return ord(c)-64

def total_name_scores(names):
    total = 0
    for pos, name in enumerate(names):
        score = 0
        for char in name:
            score += alpha_val(char)
        score *= (pos+1)
        total += score
    return total

# get names into list and format, sort
names = []
with open("p022.txt", "r") as f:
    names = f.readline().split(",")
names = sorted([x.strip('"') for x in names])

print(total_name_scores(names))