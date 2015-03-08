# Steve Beal
# Project Euler problem 39 solution
# 3/8/15

# If p is the perimeter of a right angle triangle with integral side lengths
# {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p <= 1000, is the number of solutions maximised?

def max_right_triangle_perimeter(perimeter):

    # Helpful expressions and constraints:
    # (1) a + b + c = p
    # (2) a^2 + b^2 = c^2
    # (3) a < b < c (avoids counting valid side lengths in a different order)
    # (4) a < p / 3 (implied by (1) and (3))

    # We already know we'll be varying a and p, so if we can write b or c in
    # terms of a and p, we can derive the other. Let's solve for b.
    # Rewrite (1) to c = p - a - b (5).
    # Replace c in (2) with (5): a^2 + b^2 = (p - a - b)^2
    # Expanding and solving for b, we get to b = (p^2 - 2pa) / (2p - 2a).
    # The values we input for a and p, and the derived value of b all satisfy
    # (1) and (2). Our last requirement is that a, b, and c are integers.
    # We know a and p are integers. If b is an integer too, c must also be an
    # integer. So we check whether b is an integer before counting a valid
    # solution for the given perimeter.

    max_sols = 0
    max_p = 0

    # p must be >= 3 since we have 3 sides of length >= 1
    for p in range(3, perimeter+1):
        sols = 0
        p_squared = p**2

        for a in range(1, (p+2) // 3):
            b = (p_squared - (2*p*a)) / (2*p - 2*a)
            if b % 1 == 0:
                sols += 1

        if sols >= max_sols:
            max_sols = sols
            max_p = p

    return max_p


print(max_right_triangle_perimeter(1000))