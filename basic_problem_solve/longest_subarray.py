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

def end_of_block(arr, x, i):
    # given arr and x is a value in arr st. arr_i=x, find longest subarr x,...,x starting from i
    # ie end of the subarr
    for j in range(i, len(arr)):
        if arr[j] == x:
            pass
        else:
            return j-1
    return len(arr)-1


def find_sub_arr(arr, i):
    # given index i in arr,
    # find the contiguous block which start from i and have form eihter [a_i, ..., a_i, a_i + 1,..., a_i + 1],
    # or a_i, ..., a_i, a_i - 1,..., a_i - 1
    # Return len of that block

    # find end of sub_arr of form a_i, .., a_i
    j = end_of_block(arr, arr[i], i)

    if j+1 < len(arr):
        if abs(arr[j + 1] - arr[i]) == 1:
            k = end_of_block(arr, arr[j + 1], j + 1)
            return k - i + 1
        else:
            return j - i + 1
    else:
        return j-i+1


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
