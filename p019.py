# Steve Beal
# Project Euler problem 19 solution
# 2/15/14

# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days have September,
# April, June, and November.
# All the rest have thirty-one, 
# Saving February alone, 
# Which has twenty-eight, rain or shine
# And on leap years, twenty-nine

# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

reg_month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):
	if year % 4 == 0:
		if year % 100 != 0:
			return True
		else:
			if year % 400 == 0:
				return True
			else:
				return False
	else:
		return False

# first sunday date (month indexed from 0)
day = 6
month = 0
year = 1901

first_sundays = 0

# gets the first sunday in 1901
while year < 2001:
	# check if we're in feb of a leap year
	if month == 1 and is_leap_year(year):
		month_days = leap_month_days
	else:
		month_days = reg_month_days

	# get the next sunday
	day += 7

	# advance the month
	if day > month_days[month]:
		day %= month_days[month]
		month += 1

	# advance the year
	if month > 11:
		month %= 12
		year += 1

	# count the sundays that are the first of the month	
	if day == 1:
		first_sundays += 1

print first_sundays