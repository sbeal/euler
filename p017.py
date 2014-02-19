# Steve Beal
# Project Euler problem 17 solution
# 2/12/14

# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3+3+5+4+4=19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive are written out
# in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of
# "and" when writing out numbers is in compliance with British usage.

under_20_len = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6,
			    12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}

tens_place_len = {2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}

len_hundred = 7
len_thousand = 8
len_and = 3

total_letters = 0
for i in range(1, 1001):
	if i > 0 and i <= 9999:
		# do thousands place
		if i >= 1000:
			total_letters += len_thousand + under_20_len[i/1000]
			i %= 1000
		if i >= 100:
			total_letters += len_hundred + under_20_len[i/100]
			if i % 100 != 0:
				total_letters += len_and
			i %= 100
		if i >= 20:
			total_letters += tens_place_len[i/10]
			i %= 10
		if i in under_20_len:
			total_letters += under_20_len[i]
	else:
		print "Invalid limit..."
		break

print total_letters