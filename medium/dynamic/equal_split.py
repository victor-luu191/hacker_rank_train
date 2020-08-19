#!/bin/python3

import os


def find_uniq_values(arr):
    uniq_values = []
    for v in arr:
        if v not in uniq_values:
            uniq_values.append(v)
    return uniq_values

def equal(arr):
    # return min no. of ops needed to equalize all elements in arr
    # in each operation, she can give x chocolates to some n-1 colleagues, where x in [1,2 or 5]
    # so right bf the last op, n-1 colleagues must have the same chocolates,
    # which equals to the chocolates of the remaining colleague minus x, so arr = [a-x, ..., a-x, a]

    uniq_values = sorted(find_uniq_values(arr))
    min_v = uniq_values[0]
    m = len(uniq_values)
    # if all elements equal, do nothing
    if m == 1:
        return 0

    # else,
    # must increase the smallest value min_v to reach some value,
    #  thus reducing at least 1 inequal.
    n_ops = []
    for i in range(1, m):
        value = uniq_values[i]
        fix_idx = arr.index(value)
        diff = value - min_v
        new_arr = [arr[i] + diff for i in range(fix_idx)] + [arr[fix_idx]] + \
                  [arr[i] + diff for i in range(fix_idx + 1, n)]
        n_ops.append(cal_min_ops(diff) + equal(new_arr))
    return min(n_ops)


def cal_min_ops(diff):
    i = diff // 5
    r = diff % 5
    j = r // 2
    k = r % 2
    min_ops = i + j + k
    return min_ops


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

# # suppose a_i is the value for which a0 need least ops to reach , then
# # we will make all colleagues with a0 bars become ai, thus reducing at least 1 inequal.
# # Find such i
# min_ops, best_i = -1, 0
# for i in range(1, m):
#     v = uniq_values[i]
#     ops = cal_min_ops(v - min_v)
#     if ops < min_ops:
#         min_ops = ops
#         best_i = i
#
# # we fix a single colleague with ai bars, and add to others ai - a0 bars,
# # thus all colleagues with a0 bars become ai bars
# sort_arr = sorted(arr)
# value = uniq_values[best_i]
# fix_idx = sort_arr.index(value)
# diff = value - min_v
# n = len(arr)
# new_arr = [sort_arr[i] + diff for i in range(fix_idx)] + [sort_arr[fix_idx]] + \
#           [sort_arr[i] + diff for i in range(fix_idx + 1, n)]
# return min_ops + equal(new_arr)
