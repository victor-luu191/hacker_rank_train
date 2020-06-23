#!/bin/python3

import os


def power_sum_lb(x, n, lb=1):
    # return no. of ways X can be written as a sum of N powers of unique naturals,
    # the first number must be more than the lower bound lb
    # each such natural must not exceed n-th root of X

    # NOTE: using n-th root will fail as builtin root lost precision

    # print('Trying to split', x, 'into sums of', n, 'powers')

    # stop cond
    if x == 0:
        # print('\t split successfully')
        return 1

    if lb ** n > x:
        # print('\t split failed')
        return 0
    else:
        n_ways = 0
        i = lb
        while i ** n <= x:
            # print(x, '=', i, '^{} +...'.format(n))
            n_ways += power_sum_lb(x - i ** n, n, lb=i + 1)
            i += 1
        return n_ways


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = power_sum_lb(X, N, lb=1)

    fptr.write(str(result) + '\n')

    fptr.close()
