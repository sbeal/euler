# Steve Beal
# Project Euler problem 13 solution
# 2/4/14

# Work out the first 10 digits of the sum of the following one-hundred 50-digit numbers
# (numbers omitted)

lines = []
with open("p013.txt") as f:
    line = f.readline()
    while line:
        lines.append(long(line.strip()))
        line = f.readline()
        
x = sum(lines)
print str(x)[:10]

# or to avoid converting the number to a string, take advantage of the fact
# that any 10-digit number > 999,999,999 and repeatedly divide by 10
while x > 9999999990:
    x /= 10
print x