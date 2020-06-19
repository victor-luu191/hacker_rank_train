#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    # return perm P of [1:n] s.t. |p_i - i| = k, for all i in [1:n]
    # return -1 if not possible
    # idea: a must is that k <= n/2
    # as p_i can only be i +/- k and p_i must be in range 1:n, we must have
    # p_i = i + k for i in [1:k] and p_i = i - k for i in [n-k:n]
    # esp p(n-k+1) = n-2k+1 and must be at least 1 so n-2k >= 0 so k<= n/2

    if k > n/2:
        return -1

    p = [0]*n
    for i in range(1, k+1):
        p[i] = i + k
    for i in range(n-k+1, n+1):
        p[i] = i-k
    
    # hard part when i in (k+1) : (n-k)
    # as p_i is either i-k or i+k, two possibities, brute-force is to try all
    # totally 2^(n-2k) cases


    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
