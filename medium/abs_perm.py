#!/bin/python3

import os


# Complete the absolutePermutation function below.
def make_arrays(start, stop, k):
    # given start and stop index (start <= stop), and k,
    # return all arrays a s.t. a_i is either i+k or i-k for all i in start:stop inclusive
    # recursive

    # stop cond
    if start > stop:
        return [list()]

    arrays = make_arrays(start + 1, stop, k)
    return [[start - k + 1] + a for a in arrays] + [[start + k + 1] + a for a in arrays]


def is_perm(arr, n):
    # given n and an arr of len n, check if it is a permutation of 1:n
    sort_a = sorted(arr)
    for i in range(n):
        if sort_a[i] != i + 1:
            print('not a perm of 1:', n)
            return False

    print('is a perm of 1:n')
    return True


def absolutePermutation(n, k):
    # return perm P of [1:n] s.t. |p_i - i| = k, for all i in [1:n]
    # return -1 if not possible
    # idea: a must is that k <= n/2
    # as p_i can only be i +/- k and p_i must be in range 1:n, we must have
    # p_i = i + k for i in [1:k] and p_i = i - k for i in [n-k:n]
    # esp p(n-k+1) = n-2k+1 and must be at least 1 so n-2k >= 0 so k<= n/2

    if k > n / 2:
        return [-1]

    # Trivial case when k=0
    if k == 0:
        return range(1, n + 1)

    # Non-trivial cases
    p = [0] * n
    for i in range(k):
        p[i] = i + k + 1
    for i in range(n - k, n):
        p[i] = i - k + 1

    # hard part when i in k : (n-k-1) inclusive
    # as p_i is either i-k or i+k, two possibities, brute-force is to try all
    # totally 2^(n-2k) cases

    # make all such cases
    arrays = make_arrays(k, n - k - 1, k)
    for a in arrays:
        for i in range(k, n - k):
            p[i] = a[i - k]
        print('perm: ', p)
        if is_perm(p, n):
            return p
    return [-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # fptr = open("my_out_02.txt", 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
