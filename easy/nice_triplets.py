#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the beautifulTriplets function below.
def count(x, arr):
    # count occurence of x in increasing arr
    c = 0
    for i in range(len(arr)):
        if arr[i] == x:
            c += 1
        if arr[i] > x:
            return c
    return c


def findNiceTriplets(d, arr):
    # find nice triplets starting with a[0], with diff d
    # then the triplet is a[0], a[0]+d, a[0]+2d.
    # Once all three values occur then
    # number of such triplet is max(count(a[0]) , count(a[0]+d), count(a[0]+2d))
    # Else the number is 0
    c0 = count(arr[0], arr)
    c1 = count(arr[0] + d, arr)
    c2 = count(arr[0] + 2 * d, arr)
    # debug
    # print('count of ', arr[0], ': ', c0)
    # print('count of ', arr[0] + d, ': ', c1)
    # print('count of ', arr[0] + 2 * d, ' :', c2)

    if all([c0 > 0, c1 > 0, c2 > 0]):
        res = max(c0, c1, c2)
    else:
        res = 0

    print('number of nice triplets starting with ', arr[0], ': ', res)
    return res


def beautifulTriplets(d, arr):
    # return the number of nice triplets
    res = 0

    counted = []    # keep track of items which we have counted to avoid dup counts
    for i in range(len(arr)):
        if arr[i] not in counted:
            res += (findNiceTriplets(d, arr[i:]))
            counted += [arr[i]]
    return res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
