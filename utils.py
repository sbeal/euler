# Steve Beal
# Utility module for project euler solutions
# 1/31/14

from math import sqrt, factorial
from random import *
import re

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
    primes = []
    for i in range(2, n+1):
        if i not in multiples:
            primes.append(i)
            multiples.update(range(i**2, n+1, i))
    return primes


def triangle_numbers(n):
    '''Returns a list of the first n triangle numbers.'''
    triangle = [1]
    for i in range(1,n):
        triangle.append(triangle[i-1]+i+1)
    return triangle


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
