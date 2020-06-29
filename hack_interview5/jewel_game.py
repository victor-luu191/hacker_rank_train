#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMaxScore' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING jewels as parameter.
#


def find_first_repeated_block(s):
    # given a string s,
    # return the first block of repeated gems, ie. its starting index and its len
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            start = i
            # find the len of block
            for j in range(start, len(s) - 1):
                if s[j] != s[j + 1]:  # end of block
                    length = j - start + 1
                    print('first repeated block starts at:', start, 'and have len:', length)
                    return start, length

    # no block of repeated gems
    return None, None


def getMaxScore(jewels):
    # If adjacent jewels are of the same type, you can gain 1 point by collecting them
    # (thus removing them from the sequence).

    # stop conds: either
    # i) no more jewels
    # ii) no more pair to collect, even when there are still jewels
    if len(jewels) == 0:
        return 0

    # based on analysis, we do not need to try all options,
    # any time we meet adjacent dups, can go ahead and delete them
    # so can just collect the first duplicated pair (or even block)

    start, length = find_first_repeated_block(jewels)

    if start:
        # return 1 + getMaxScore(jewels[:start] + jewels[start + 2:])
        return 1 + getMaxScore(jewels[:start] + jewels[start + length:])
    else:
        return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        jewels = input()

        ans = getMaxScore(jewels)

        fptr.write(str(ans) + '\n')

    fptr.close()
