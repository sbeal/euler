# Steve Beal
# Project Euler problem 42 solution
# 3/9/15

# The nth term of the sequence of triangle numbers is given by, t_n = n/2(n+1);
# so the first ten triangle numbers are: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55

# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10. If the word
# value is a triangle number then we shall call the word a triangle word.

# Using p042.txt, a 16K text file containing nearly two-thousand common English
# words, how many are triangle words?

from utils import n_triangulars

def word_value(word):
    val = 0
    for c in word:
        val += (ord(c) - 64)
    return val

def num_triangle_words():
    filename = "p042.txt"
    num = 0
    with open(filename, "r") as f:
        words = [w.strip('"') for w in f.readline().split(",")]
        vals = [word_value(w) for w in words]

        # Manual checking indicates that the max word value in the file is
        # 192. Manipulating the recurrence for t_n, we get n^2 + n = 384. If
        # n is 20, n^2 is 400, so 20 triangle numbers will be sufficient to
        # match any word value from the file.
        triangles_20 = set(n_triangulars(20))

        for val in vals:
            if val in triangles_20:
                num += 1
    return num


print(num_triangle_words())