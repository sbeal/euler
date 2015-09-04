# Steve Beal
# Utility module for project euler solutions
# 1/31/14

from math import sqrt, factorial
from random import *
import re
from timeit import timeit

PRIMES_BELOW_100 = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

def is_prime(n):
    '''Returns whether n is prime using a trial division method.
    Note: this is much faster than the Miller-Rabin test for small n.'''
    if n < 2:
        return False

    if n in PRIMES_BELOW_100:
        return True

    if n % 2 == 0:
        return False

    m = int(sqrt(n))
    for i in range(3, m+1, 2):
        if n % i == 0:
            return False
    return True


def is_probably_prime(n):
    '''Returns whether n is very probably prime, or not, by first checking
    against a list of known primes, then using the Miller-Rabin test
    10 times to determine composite-ness.'''

    if n < 2:
        return False

    if n in PRIMES_BELOW_100:
        return True

    # number of rounds to run the test
    k = 10

    # choose d such that n-1 = d * 2**s
    d = n-1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    assert 2**s * d == n-1

    for _ in range(k):
        a = randint(2, n-2)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue

        for _ in range(s-1):
            x = pow(x, 2, n)
            if x == 1 or x == n-1:
                break
        if x == n-1:
            continue
        else:
            return False
    return True


def is_palindrome(s):
    '''Return whether s is a palindrome, but only consider word characters as
    defined by the Python regular expression class "\w".'''
    s = s.lower()
    s = re.sub(r'\W', "", s)
    return s == s[::-1]


def is_numeric_palindrome(n):
    '''Return whether a number n is a palindrome.'''
    rev = 0
    k = n
    while k > 0:
        right_digit = k % 10
        rev = rev*10 + right_digit
        k //= 10
    return n == rev

def gcd(a, b):
    '''Returns the greatest common divisor of a and b, using 
    Euclid's gcd algorithm.'''
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, *args):
    '''Returns the least common multiple of a and any other numbers passed in.'''
    for arg in args:
        for b in arg:
            a = (a*b) // gcd(a,b)
    return a


def factor(n):
    '''Get a list of the factors of n, first checking for primality, then for
    individual factors.
    Note: could be more efficienct by combining is_prime(n) call with the
    individual factor checking, since both excecute some of the same code.'''
    if n == 1:
        return [1]
    if is_prime(n) or is_probably_prime(n):
        return [1, n]

    factors = set()
    d = 1
    while d < sqrt(n+1):
        q, r = divmod(n, d)
        if r == 0:
            factors.add(d)
            if d != q:
                factors.add(q)
        d += 1
    return factors


def prime_sieve(n):
    '''Returns a list of primes up to n using the Sieve of Eratosthenes.'''
    multiples = set()
    primes = [2]
    for i in range(3, n+1, 2):
        if i not in multiples:
            primes.append(i)
            multiples.update(range(i**2, n+1, i))
    return primes


def n_triangulars(n):
    '''Returns a list of the first n triangle numbers according to the
    relation T_n = T_(n-1) + n + 1.'''
    # this was tested and is faster than a list comprehension calling
    # nth_triangular n times
    triangle = [1]
    for i in range(1, n):
        triangle.append(triangle[i-1]+i+1)
    return triangle

def nth_triangular(n):
    '''Returns the nth triangular number according to the formula n(n+1)/2.'''
    return int(n * (n + 1) * 0.5)

def triangular_gen():
    '''Generator for individual value in triangular number sequence.'''
    n = t = 1
    while True:
        yield t
        n += 1
        t = nth_triangular(n)

def prime_factorize(n):
    '''Returns a list of tuples (b, e) where b is the prime factor
    and e is the exponent of that factor. Taking the product of 
    raising each b to its e gives the original n.'''
    factors = []
    i = 0
    d = 2
    # divide by 2 as many times as possible
    while n % d == 0:
        i+=1
        n //= d
    if i > 0:
        factors.append((d,i))

    # start dividing by odd factors (since no more evens are prime),
    # as long as they're still below the sqrt bound
    bound = sqrt(n+1)
    d = 3
    while d <= bound:
        i = 0
        while n % d == 0:
            i+=1
            n //= d
            bound = sqrt(n+1)
        if i > 0:
            factors.append((d,i))
        d += 2

    if n != 1:
        factors.append((n,1))

    return factors


def collatz(n):
    '''Returns the number following n after applying one of the 
    cases defined in the Collatz problem.'''
    if n <= 1:
        return n

    if n % 2 == 0:
        return n//2
    else:
        return 3*n + 1


def nCk(n,k):
    '''Returns the binomial coefficient n choose k.'''
    return factorial(n) // (factorial(k) * factorial(n-k))


def pascal_triangle(n):
    '''Returns list of rows 0...n of Pascal's triangle.
    Note: could be optimized to only keep track of previous row,
    rather than the whole triangle, if the goal was to print the triangle or
    return a single row.'''
    pascal = [[1]]
    for row in range(1,n+1):
        prev_row = pascal[row-1]
        len_prev = len(prev_row)
        new_row = []
        for i in range(len_prev+1):
            if i == 0 or i == len_prev:
                new_row.append(1)
            else:
                new_row.append(prev_row[i-1] + prev_row[i])
        pascal.append(new_row)
    return pascal

def fib_gen():
    '''Generator for individual value in Fibonacci sequence.'''
    a = b = 1
    while True:
        yield a
        a, b = b, a+b


def fibonacci(n):
    '''Returns the first n values in the Fibonacci sequence.'''
    fib = []
    if n < 1:
        return []
    else:
        f = fib_gen()
        for i in range(n):
            fib.append(next(f))
        return fib

def sum_proper_divisors(n):
    '''Returns the sum of all the proper divisors of n. Relies on the fact
    that for the prime factorization of n (p_1^a_1)...(p_k^a_k), the sum of
    divisors is the (p_1^0)(p_1^1)...(p_1^a_1) + ... + (p_k^0)...(p_k^a_k).'''
    total = 1
    for b,e in prime_factorize(n):
        s = 0
        while e >= 0:
            s += b**e
            e -= 1
        total *= s
    return total - n

def permutations(s):
    '''Returns a list of all permutations of a string s.'''
    if len(s) <= 1:
        return [s]

    sub_perms = permutations(s[1:])
    first = s[0]
    perms = []
    for perm in sub_perms:
        for i in range(len(perm)+1):
            perms.append(perm[:i] + first + perm[i:])
    return perms

def nth_pentagonal(n):
    '''Returns the nth pentagonal number according to the formula P_n = n(3n-1)/2.'''
    return int(n * (3*n - 1) * 0.5)

def n_pentagonals(n):
    '''Returns a list of the first n pentagonal numbers according to the
    relation P_n - P_(n-1) + 3n + 1.'''
    # this was tested and is faster than a list comprehension calling
    # nth_pentagonal n times
    pentagon = [1]
    for i in range(1, n):
        pentagon.append(pentagon[i-1] + 3*(i) + 1)
    return pentagon

def pentagonal_gen():
    '''Generator for individual value in pentagonal number sequence.'''
    n = p = 1
    while True:
        yield p
        n += 1
        p = nth_pentagonal(n)

def is_pentagonal(x):
    '''Returns whether x is a pentagonal number by trying to solve x = n(3n-1)/2 for n.'''
    if x < 1:
        return (False, "x < 1")

    # x = n(3n-1)/2
    # 2x = 3n^2-n
    # 3n^2 - n - 2x = 0
    # a = 3, b = -1, c = -2x
    # d = b^2 - 4ac

    a, b, c = 3, -1, -2*x
    d = discriminant(a, b, c)

    if d < 0:
        # no real roots
        return False
    elif d == 0:
        # two coincident real roots -b / 2a
        root = one_real_root(a, b)
        if root > 0 and float.is_integer(root) and nth_pentagonal(root) == x:
            return True
    else:
        # two distinct real roots (-b +- sqrt(d)) / 2a (quad formula)
        root1, root2 = two_real_roots(a, b, d)
        if root1 > 0 and float.is_integer(root1) and nth_pentagonal(root1) == x:
            return True
        elif root2 > 0 and  float.is_integer(root2) and nth_pentagonal(root2) == x:
            return True

    return False

def discriminant(a, b, c):
    return b*b - (4*a*c)

def one_real_root(a, b):
    return -b / 2*a

def two_real_roots(a, b, d):
    root1 = (-1*b + sqrt(d)) / (2*a)
    root2 = (-1*b - sqrt(d)) / (2*a)
    return (root1, root2)

def nth_hexagonal(n):
    '''Returns the nth hexagonal number according to the formula H_n = n(2n-1).'''
    return n*(2*n - 1)

def n_hexagonals(n):
    '''Returns a list of the first n hexagonal numbers according to the
    relation H_n = H_(n-1) + 4n + 1.'''
    # this was tested and is faster than a list comprehension calling
    # nth_hexagonal n times
    hexagon = [1]
    for i in range(1, n):
        hexagon.append(hexagon[i-1] + 4*i + 1)
    return hexagon

def hexagonal_gen():
    '''Generator for an individual value in the hexagonal number sequence.'''
    n = h = 1
    while True:
        yield h
        n += 1
        h = nth_hexagonal(n) 

def is_hexagonal(x):
    '''Returns whether x is a hexagonal number by trying to solve x = n(2n-1) for n.'''
    if x < 1:
        return False

    # x = n(2n-1)
    # 2n^2 - n - x = 0
    # a = 2, b = -1, c = -x
    # d = b^2 - 4ac
    a, b, c, = 2, -1, -x
    d = discriminant(a, b, c)

    if d < 0:
        # no real roots
        return False
    elif d == 0:
        # one real root
        root = one_real_root(a, b)
        if root > 0 and float.is_integer(root) and nth_hexagonal(root) == x:
            return True
    else:
        # two real roots
        root1, root2 = two_real_roots(a, b, d)

        if root1 > 0 and float.is_integer(root1) and nth_hexagonal(root1) == x:
            return True
        elif root2 > 0 and  float.is_integer(root2) and nth_hexagonal(root2) == x:
            return True

    return False

def time_function(function, iterations=1):
    if iterations > 0:
        total = timeit(function.__name__ + "()", setup="from __main__ import " + function.__name__, number=iterations)
        average = total / iterations
        return (total, average)
    return 0
