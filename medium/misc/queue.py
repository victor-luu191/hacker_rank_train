#!/bin/python3

import math
import os
import random
import re
import sys


# each person can bribe max two persons directly in front of him, so a person can move forward at most 2 positions, any seq violating this is invalid. at first, i person stay at i index, so i > 2 can only be moved fw to either i-1 or i-2. but i can be moved bw as far as possible, by keep swapping it with the person behind. So i can be only in range [i-2, n]. Esp n can only be at 1 of 3 positions n-2, n-1, n.
# if q_n = n, ie. in final state n is still at last pos, the best way is that he made no bribe at all, so min_bribe(q) = min_bribe(q\n)
# if ...

# CONST = 10**6
def minimumBribes(q):
    res = min_bribe(q)
    if res < 0:
        print('Too chaotic')
    else:
        print(str(res))


def min_bribe(q):
    m = len(q)
    print('queue length:', m)
    # stop cond
    if m == 1:
        return 0
    if m == 2:
        if q == [1, 2]:
            return 0
        else:
            return 1

    if m > 2:
        pos_of_m = q.index(m) + 1
        if pos_of_m < m - 2:
            return -1
        if pos_of_m == (m - 2):  # n made 2 bribes to move fw 2 positions and q[n-3]=n
            others = q[:(m - 3)] + q[m - 2:]
            other_bribes = min_bribe(others)
            if other_bribes >= 0:
                return other_bribes + 2
            else:
                return -1  # propagate the invalid till outmost caller
        if pos_of_m == m - 1:  # n made >=1 bribe and q[n-2] = n
            others = q[:(m - 2)] + q[m - 1:]
            other_bribes = min_bribe(others)
            if other_bribes >= 0:
                return other_bribes + 1
            else:
                return -1
        if pos_of_m == m:  # n is still at last pos, the best way: he not bribe and only others move
            others = q[:(m - 1)]
            other_bribes = min_bribe(others)
            if other_bribes >= 0:
                return other_bribes
            else:
                return -1


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
