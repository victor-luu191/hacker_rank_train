#!/bin/python3

import os
import string

UPPERS = string.ascii_uppercase
def del_lower(a):
    return [ch for ch in a if ch in UPPERS]


# Complete the abbreviation function below.
def abbreviation(a, b):
    # stop cond
    if not b:
        # just delete all lowercase letters from a
        a_left = del_lower(a)
        if not a_left:
            return 'YES'
        else:
            return 'NO'
    if not a:
        return 'NO'

    # Match b[0]
    # find first letter in a which can be matched with b0, either as is or via capitalize
    idx = find_1st_letter_matchable(a, b[0])
    if idx < 0: # no matchable letter
        return 'NO'

    # there is a matching letter at idx,
    # First need to drop all letters bf idx as they are unmatchable,
    # however we may not be able to drop all of them, as only allowed to drop lower letters,
    # UPPER letters will be left => so cannot match
    left = del_lower(a[:idx])
    if left:
        return 'NO'

    # successfully delete all unmatched letters,
    # left is a[idx:], as a[idx] is matched to b[0] already, just need to check matching for remains of a and b
    return abbreviation(a[idx + 1:], b[1:])


def find_1st_letter_matchable(a, ch):
    if (ch in a) and (ch.lower() in a):
        return min(a.index(ch), a.index(ch.lower()))
    if (ch in a) and (not ch.lower() in a):
        return a.index(ch)
    if (not ch in a) and (ch.lower() in a):
        return a.index(ch.lower())
    if (ch not in a) and (ch.lower() not in a):
        return -1


if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except PermissionError:
        fptr = open('../abbr-testcases/output/test3.txt', 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
