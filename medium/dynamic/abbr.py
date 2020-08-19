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
    first_matches = find_1st_matches(a, b[0])
    if not first_matches:  # no matchable letter
        return 'NO'

    res = []
    for i in first_matches:
        r_i = match_first_letter(b, a, i)
        res.append(r_i)
    if 'YES' in res:
        return 'YES'
    return 'NO'


def match_first_letter(b, a, i):
    # Given that b[0] can be matched with a[i], check if a[i+1:] can match with b[1:]

    # First need to drop all letters bf idx i as they are unmatchable,
    # however we may not be able to drop all of them, as only allowed to drop lower letters,
    # UPPER letters will be left => so cannot match
    left = del_lower(a[:i])
    if left:
        return 'NO'
    # successfully delete all unmatched letters,
    # left is a[idx:], as a[idx] is matched to b[0] already,
    print('a[idx] is', a[i])
    print('b[0]:', b[0])
    # just need to check matching for remains of a and b
    a_rem = a[i + 1:]
    b_rem = b[1:]
    print('remain of a:', a_rem)
    print('remain of b:', b_rem)
    return abbreviation(a_rem, b_rem)


def find_1st_matches(a, ch):
    if (ch in a) and (ch.lower() in a):
        return [a.index(ch), a.index(ch.lower())]
    if (ch in a) and (not ch.lower() in a):
        return [a.index(ch)]
    if (not ch in a) and (ch.lower() in a):
        return [a.index(ch.lower())]
    if (ch not in a) and (ch.lower() not in a):
        return []


if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except PermissionError:
        t = int(input())
        fptr = open('../abbr-testcases/output/my_out_{}.txt'.format(t) , 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
