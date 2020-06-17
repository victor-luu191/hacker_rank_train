#!/bin/python3
import bisect
import math
import os
import random
import re
import sys


# Complete the biggerIsGreater function below.

# given x and descend array dec,
# find the first position in dec st dec[j] > x
# TODO: use bisect to exploit the fact that dec already sorted descendingly
def findFirstLarger(x, dec):
    for j in reversed(range(len(dec))):
        if dec[j] > x:
            return j

    return -1


def biggerIsGreater(w):
    # obs: as we want to find the closest larger, we need to change w in backward direction, like handle units first
    # if w is already in descending order then it is already the largest possible, thus no answer.
    # else go backward, until reach the first index i where w[i] <  w[i+1], then
    # swap w[i] with the first/smallest letter larger than it in w[i+1:],

    # first need to convert to list, as direct assign cause bug
    # as str are immutable in python
    s = list(w)

    found, i = findAscendIndex(s)
    if not found:  # already in desc order, no answer
        return 'no answer'
    else:
        print('first index with ascend order: ', i)
        print(s[i], s[i + 1])
        # find the first/smallest letter larger than it in s[i+1:]
        j = findFirstLarger(s[i], s[i + 1:]) + i + 1
        print('first letter larger than ', s[i], ' is letter ', s[j], ' at position ', j, )
        # swap
        tmp = s[i]
        s[i] = s[j]
        s[j] = tmp

        part1 = s[:i + 1]
        # sort s[i+1:] in ascending to ensure minimum
        part2 = list(sorted(s[i + 1:]))
        return ''.join(part1 + part2)


def findAscendIndex(s):
    n = len(s)
    for i in reversed(range(n - 1)):
        if s[i] < s[i + 1]:
            found = True
            return found, i
    return False, -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
