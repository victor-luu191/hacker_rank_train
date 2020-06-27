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

def find_start_of_adjacent_dups(s):
    # given a string, return the list of all pairs of adjacent dups,
    # for each such pair return its start idnex

    indices = []
    for i in range(len(s)-1):
        if s[i] == s[i + 1]:
            indices.append(i)

    return indices


def getMaxScore(jewels):
    # If adjacent jewels are of the same type, you can gain 1 point by collecting them
    # (thus removing them from the sequence).

    # stop conds: either
    # i) no more jewels
    # ii) no more pair to collect, even when there are still jewels
    if len(jewels) == 0:
        return 0

    indices = find_start_of_adjacent_dups(jewels)
    if indices:
        # based on analysis, we do not need to try all options,
        # any time we meet adjacent dups, can go ahead and delete them
        # so can collect the first duplicated pair (or even block)
        i = indices[0]
        return 1 + getMaxScore(jewels[:i] + jewels[i + 2:])

        ## try all possible ways of collecting gems
        # scores = []
        # for i in indices:  # find max score if start by collecting pair j[i], j[i+1]
        #     score_i = 1 + getMaxScore(jewels[:i] + jewels[i + 2:])
        #     scores.append(score_i)
        # return max(scores)
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
