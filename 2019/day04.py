#!/usr/bin/env python3

"""
--- Day 4: Secure Container ---

You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

Other than the range rule, the following are true:

    111111 meets these criteria (double 11, never decreases).
    223450 does not meet these criteria (decreasing pair of digits 50).
    123789 does not meet these criteria (no double).

How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 278384-824795.
"""

min, max = 278384, 824795

def valid_password(p):
    s = str(p)
    l = len(s)

    # It is a six-digit number.
    if l != 6:
        return False
    # The value is within the range given in your puzzle input.
    if p < min or p > max:
        return False
    # Two adjacent digits are the same (like 22 in 122345).
    i, hasAdjacent = 0, False
    while i < (l - 1):
        if s[i] == s[i + 1]:
            hasAdjacent = True
            break
        i += 1
    if hasAdjacent == False:
        return False
    # Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
    ints, j = [int(c) for c in s], 0
    while j < (l - 1):
        if ints[j] > ints[j + 1]:
            return False
        j += 1

    return True

password, count = min, 0
while password <= max:
    if valid_password(password):
        # print('combo: {}'.format(password))
        count += 1
    password += 1

print(' :: total valid combos => {}'.format(count))
