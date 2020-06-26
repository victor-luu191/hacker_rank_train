#!/bin/python3

import os


#
# Complete the 'maxXorValue' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING x
#  2. INTEGER k
#

def maxXorValue(x, k):
    # return y s.t.
    # i) y has at most k 1-bits and,
    # ii) x bitwise XOR y is max
    # as xor return 1 when two bits differ, we want bits of y differ from corresponding bits of x as much as possible,
    # to maximize result the diff should happen at most significant positions, i.e. bits from the left
    # thus, need to maximize 1st bit in result, then maximize remain -> recur

    # stop cond
    if k == 0:
        return ''.zfill(len(x))
        # return ''.join(['0'] * len(x))
    if len(x) == 0:
        return ''

    if k > 0 and len(x) > 0:  # y0 can be 1
        y0 = 1 - int(x[0])  # s.t. y0 differ from x0
        if y0 == 0:
            return ''.join(['0', maxXorValue(x[1:], k)])
        else:
            return ''.join(['1', maxXorValue(x[1:], k - 1)])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        k = int(input().strip())

        y = maxXorValue(s, k)

        fptr.write(y + '\n')

    fptr.close()
