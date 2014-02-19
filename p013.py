# Steve Beal
# Project Euler problem 13 solution
# 2/4/14

# Work out the first 10 digits of the sum of the following one-hundred 50-digit numbers
# (numbers omitted)

lines = []
with open("p13.txt") as f:
	line = f.readline()
	while line:
		lines.append(long(line.strip()))
		line = f.readline()

		
print str(sum(lines))[:10]
