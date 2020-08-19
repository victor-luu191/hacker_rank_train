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

def dyn_get_ways(n, coins):
    # Overlap can also happen, as we may need to compute getWays(k, c) twice,
    # so we need to avoid it via dynamic programming,
    # ie. use an array to store values already computed and we go from small to large amount
    # for 0 <= i <= n and 1 <= k <= m,
    # let ways[i, k] = number of ways to change amount i using k last coins,
    # then what we need is ways[n, m]
    # ways[i, k] = sum_j ways[i - coins[-j], j], for j in [1:k]
    print('sorted coins:', coins)
    m = len(coins)
    # ways = np.zeros((n+1, m))
    rows, cols = n + 1, m + 1
    ways = [[0 for i in range(cols)] for j in range(rows)]
    ways[0] = [1] * (m + 1)
    min_coin = coins[0]
    for i in range(min_coin, n + 1):
        for k in range(1, m + 1):
            for j in range(1, k + 1):
                if not (coins[-j] > i):
                    ways[i][k] += ways[i - coins[-j]][j]

    return ways[n][m]


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

    sorted_coins = sorted(coins)
    return dyn_get_ways(n, sorted_coins)


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
