#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'longestSubarray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def find_end_of_block(i, arr):
    # given index i, find longest subarray starting from i and having form a_i,...,a_i
    # ie return end of the subarr a_i,...,a_i
    for j in range(i, len(arr)):
        if arr[j] == arr[i] :
            pass
        else:
            end_of_block = j - 1
            # print('starting from ', i, '-index, sub-array with all values equal ', arr[i], ' extend to ', end_of_block)
            # print('the sub-array', arr[i:j])
            return end_of_block

    # print('starting from ', i, '-index, sub-array with all values equal ', arr[i], ' extend to end of array')
    return len(arr)-1


def find_sub_arr(arr, i):
    # given index i in arr,
    # find the contiguous block which start from i and have form either [a_i, ..., a_i, a_i + 1,..., a_i + 1],
    # or a_i, ..., a_i, a_i - 1,..., a_i - 1
    # Return len of that block

    # basically, such a block is made from 2 blocks [a_i,..., a_i] and [a_i +/- 1, ..., a_i +/- 1]
    # which are next to each ohter

    # find end of sub_arr starting from i and of form a_i, .., a_i
    j = find_end_of_block(i, arr)

    if j+1 < len(arr):
        # find block [a_i +/- 1, ..., a_i +/- 1]
        if abs(arr[j + 1] - arr[j]) == 1:
            k = find_end_of_block(j + 1, arr)
            print(arr[i:k+1])
            return k - i + 1
        else:
            print(arr[i:j+1])
            return j - i + 1
    else:
        print(arr[i:j + 1])
        return j - i + 1


def longestSubarray(arr):
    # return longest subarray where distinct values differ exactly 1
    # NOTE: sub array must be a contiguous part of arr

    # for each index i,  find such a sub-array starting from i index
    # must be a contiguous block of form a_i, ..., a_i, a_i + 1,..., a_i + 1
    # or a_i, ..., a_i, a_i - 1,..., a_i - 1
    sub_lengths = []
    for i in range(len(arr)):
        s_len = find_sub_arr(arr, i)
        sub_lengths.append(s_len)

    return max(sub_lengths)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = longestSubarray(arr)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
