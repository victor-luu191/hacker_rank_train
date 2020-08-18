#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c: contain values of coins
#

def getWays(n, coins):
    # the first coin can be any value not exceeding n, say c[i],
    # then remaining coins must sum to n - c[i], so have getWays(n - c[i], c)
    # so fnal result is sth like sum_i getWays(n - c[i], c).
    # But there can be dups, eg. (1, 2) and (2, 1) is same way. how to rm dups?
    # One way is to make sure a non-decreasing order in values of coins used,
    # ie. once we use coin c[i], we do not use a coin of less value,
    # so, we need to remove from c the coins of values smaller than c[i], and
    # get c\{c[j]: j < i} (assume that the coins already sorted).
    # So formula should be: sum_i getWays(n - c[i], c\{c[j]: j < i})

    # Overlap can also happen, say we may need to compute getWays(k, c) twice,
    # so we need to avoid it via dynamic programming  (later)
    if n == 0:
        return 1  # use no coin is considered as 1 way, also we keep reducing n and when it reach 0 meaning we have a correct change

    if (n > 0) and (n < min(coins)):
        return 0
    else:
        # find values not exceeding n
        valid_coins = [c for c in coins if c <= n]

        res = 0
        for c in valid_coins:
            # we use it as the 1st coin

            # drop coins of values smaller than c
            larger = [d for d in valid_coins if d >= c]
            # as c is now the first coin, remains coins must sum to n - c
            res += getWays(n - c, larger)

        return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
