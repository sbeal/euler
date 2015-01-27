# Steve Beal
# Project Euler problem 8 solution
# 2/1/14

# Note: this problem was updated to use 13 (rather than 5) as the input
# after I first solved it. This solution now uses 13 as the input.

# Find the greatest product of five consecutive digits in the 1000-digit number.

def get_int_product(s):
    prod = 1
    for c in s:
        prod *= int(c)
    return prod


def greatest_consecutive_product_1(n, num_consec):
    # naive method - convert to string, go thru in order, convert back to int
    s = str(n)
    max_prod = 0
    for i in range(len(s)-num_consec+1):
        x = s[i:i+num_consec]
        p = get_int_product(x)
        if p > max_prod:
            max_prod = p
    return max_prod


def greatest_consecutive_product_2(n, num_consec):
    # could also go through it from right to left, keeping track of the digits
    # and multiplying (without converting to strings). this is faster, but all
    # the list slicing does not help...
    max_prod = 0
    k = n
    cur_to_multiply = []
    while len(cur_to_multiply) < num_consec:
        cur_to_multiply.append(k % 10)
        k //= 10

    while k > 0:
        prod = 1
        for p in cur_to_multiply:
            prod *= p
        if prod > max_prod:
            max_prod = prod
        cur_to_multiply = cur_to_multiply[1:] + [k % 10]
        k //= 10
    return max_prod


n = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
num_consec = 13

print(greatest_consecutive_product_1(n, num_consec))
print(greatest_consecutive_product_2(n, num_consec))