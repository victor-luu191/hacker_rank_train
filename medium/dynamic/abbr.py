#!/bin/python3

import os
import string

UPPERS = string.ascii_uppercase


def del_lower(a):
    return [ch for ch in a if ch in UPPERS]


# Complete the abbreviation function below.
def abbreviation(a, b):
    if can_match(b, a):
        return 'YES'
    else:
        return 'NO'


def can_drop_all_prev_letters(i, a):
    # given index i, check if we can drop all letters bf a[i] by dropping only lower cases
    left = del_lower(a[:i])
    return (not left)


def can_match(b, a):
    # stop cond
    if not b:
        # just delete all lowercase letters from a
        a_left = del_lower(a)
        if not a_left:
            return 1
        else:
            return 0
    if not a:
        return 0

    # Match b[0]
    # As there may be many letters in a which can be matched with b[0], either as is or via capitalize;
    # we try all such letters

    # Try the first of such letter (if have),  say at index i of a,
    #  then try matching b with a[i:] (b[0] with a[i] already), if possible then return 1, else try other poss
    # NOTE: matching b with a[i:] only leads to a final valid match if we can drop all letters bf i
    # via dropping lower cases
    i = find_1st_match(a, b[0])
    if i < 0:  # no matchable letter
        return 0
    # else
    # try matching b with a[i:]
    if not can_drop_all_prev_letters(i, a):
        return 0
    # b[0] match with a[i] already
    # check if can match b[1:] with a[i+1:]
    if can_match(b[1:], a[i + 1:]):
        return 1
    else:  # try matching b[0] with its later occurences  in a
        # todo: optimizing code
        j = find_1st_match(a[i + 1:], b[0])  # note that a is cut by i+1 items, so need to add back later
        if j < 0:
            return 0
        next_occur = j + i + 1
        if not can_drop_all_prev_letters(next_occur, a):
            return 0
        return can_match(b, a[next_occur:])

        ## work but a bit slow
        # return can_match(b, a[i+1:])



def find_1st_match(a, ch):
    # given char ch and str a, find the first letter in a which can be matched with ch,
    # either as is or via capitalize;
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
        t = int(input())
        fptr = open('../abbr-testcases/output/my_out_{}.txt'.format(t), 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
