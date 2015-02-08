# Steve Beal
# Project Euler problem 31 solution
# 2/7/15

# In England the currency is made up of pound, £, and pence, p, and there are 
# eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
# 1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
# How many different ways can £2 be made using any number of coins?

COINS = [1, 2, 5, 10, 20, 50, 100, 200]
NUM_COINS = len(COINS)

def make_change_pounds(n):
    pence = n*100

    # Here, we notice that the number of ways to make change for £n with the
    # first m coins is the number of ways to make £n with the first m-1 coins,
    # plus the number of ways to make £n-j with the first m coins, where j is
    # the value of the mth coin. For example, the number of ways to make 2p
    # with the first two coins is 2: 1p+1p and 2p. This is the sum of the
    # number of ways to make 1p with the first two coins (1: 1p) and the number
    # of ways to make 2p with the first coin (1: 1p+1p). Since this recursive
    # relationship will repeat many subproblems, we will use a dynamic
    # programming method. Note that the base cases are:
    # -- number of ways = 1 when n = 0 (the only way is to give no change)
    # -- number of ways = 0 when n < 0 or when n > 0 and m < 1 (these are
    #    the cases of having negative £ to make change for and having no
    #    coins available)

    table = [[0]*(NUM_COINS+1) for x in range(pence+1)]

    for i in range(pence+1):
        table[i][0] = 0
    for i in range(NUM_COINS+1):
        table[0][i] = 1

    for i in range(1, pence+1):
        for j in range(1, NUM_COINS+1):
            sub_prob = 0
            if i-COINS[j-1] >= 0:
                sub_prob = table[i-COINS[j-1]][j]
            table[i][j] = table[i][j-1] + sub_prob

    return table[pence][NUM_COINS]

print(make_change_pounds(2))