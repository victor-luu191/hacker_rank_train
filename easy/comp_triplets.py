#!/bin/python3

import os


# Complete the compareTriplets function below.
def compareTriplets(a, b):
    a_point, b_point = 0, 0
    for i in range(3):
        if a[i] > b[i]:
            a_point += 1
        if b[i] > a[i]:
            b_point += 1

    return [a_point, b_point]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
