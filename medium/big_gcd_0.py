#!/bin/python3

import math
import os


# Complete the 'findSubsequence' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. INTEGER k

# Find longest subseq of len at least k s.t. gcd of items in the subseq is maximal


def findGCD(arr):
    if len(arr) == 2:
        return math.gcd(arr[0], arr[1])
    else:
        return math.gcd(arr[0], findGCD(arr[1:]))


# TODO: debug this method
def subseqLen(k, arr):
    # return all subseq with len k containing arr[0]
    # stop cond
    if k == 1:
        return [[arr[i]] for i in range(len(arr))]

    subseq_ls = []
    n = len(arr)
    for i in range(1, n - k + 1):
        subseq_ls += [ [arr[0]] + ss for ss in subseqLen(k - 1, arr[i:])]

    return subseq_ls


def findSubsequence(numbers, k):
    # when adding a number to an array, gcd will reduce
    #
    local_maxima = []
    local_sols = []
    for j in range(len(numbers) - k + 1):
        nj = numbers[j]
        # among subseqs of len k and starting with numbers[j], find the one with largest gcd
        subseqs_start_with_nj = subseqLen(k, numbers[j:])
        print('subseqs of len ', k, ' and starts with ', nj, ' : ', subseqs_start_with_nj)

        # # map each subseq to its gcd
        # gcd_dict = {}
        # for i, local_sol in enumerate(subseqs_start_with_nj):
        #     gcd_dict[i] = findGCD(local_sol)

        # # find the subseq with max gcd (local max)
        # local_max_gcd = 1
        # sol_in_subseq_start_with_nj = None
        # for i in gcd_dict.keys():
        #     if gcd_dict[i] > local_max_gcd:
        #         local_max_gcd = gcd_dict[i]
        #         sol_in_subseq_start_with_nj = subseqs_start_with_nj[i]

        gcd_ls = [findGCD(ss) for ss in subseqs_start_with_nj]
        sol_in_subseq_start_with_nj, local_max_gcd = findMax(subseqs_start_with_nj, gcd_ls)
        local_sols.append(sol_in_subseq_start_with_nj)
        local_maxima.append(local_max_gcd)

    # find the max among local max
    global_sol, global_max = findMax(local_sols, local_maxima)
    return global_sol, global_max


def findMax(xs, ys):
    # given a list of xs and a list of dependent values ys, return (best_x, max_y)
    max_y = -math.inf
    best_x = None
    for x, y in zip(xs, ys):
        if y > max_y:
            max_y = y
            best_x = x
    return best_x, max_y


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    k = int(input().strip())

    # debug
    # print(subseqLen(2, numbers))

    result = findSubsequence(numbers, k)
    print('Best subseq : ', result[0], ', with largest GCD: ', result[1])

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
