#!/bin/python3

import os


# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    # return perm P of [1:n] s.t. |p_i - i| = k, for all i in [1:n]
    # return -1 if not possible
    # Idea: a must is that k <= n/2
    # as p_i can only be i +/- k and p_i must be in range 1:n, we must have
    # p_i = i + k for i in [1:k], and p_i = i - k for i in [n-k:n]
    # esp p(n-k+1) = n-2k+1 and must be at least 1 so n-2k >= 0 so k<= n/2

    # Obs: |p_i - i| = k means the abs diff between value and index in p must always be k
    # so a value can only be moved left or right to an index k units from it
    # as values 1:k cannot be moved left, they must be moved right k units.
    # moreover, as p_i = i + k for i in [1:k], we see that values k+1:2k are moved left k units.
    # So in the end, two parts 1:k and k+1:2k are swapped with each other.
    # Similar reasoning from end of array show us things will always move in blocks of len 2k,
    # and each such block the first half must swap with the 2nd half.
    # Conclusion: n must be multiple of 2k for possible, else impossible

    id_perm = [i + 1 for i in range(n)]     # plus 1 due to 1-based indexing
    if k == 0:
        return id_perm

    if n % (2 * k) != 0:
        return [-1]
    else:
        m = n // (2 * k)
        p = []
        for i in range(m):
            start = i * (2 * k)
            end = start + 2 * k
            part = id_perm[(end - k):end] + id_perm[start:(end - k)]
            p += part
        return p


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
