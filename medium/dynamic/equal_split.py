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
    # Idea:
    # Each time, must increase the smallest value min_v to reach some value, thus reducing at least
    # 1 inequal.
    # Consider two different values v and v+d, if we keep boosting them both, then the diff
    # is always d (as each time we boost them with same value). And they keep being different.
    # Thus, there must be some time that we start fixing the bigger one and boosting the smaller until
    # it reach the larger. the number of ops needed will be min_ops(d)

    uniq_values = sorted(find_uniq_values(arr))
    min_v = uniq_values[0]
    m = len(uniq_values)
    # if all elements equal, do nothing
    if m == 1:
        return 0

    # else,
    next_value = uniq_values[1]
    sort_arr = sorted(arr)
    fix_idx = sort_arr.index(next_value)
    diff = next_value - min_v
    new_arr = (fix_idx + 1) * [sort_arr[fix_idx]] + \
              [sort_arr[i] + diff for i in range(fix_idx + 1, n)]
    return cal_min_ops(diff) + equal(new_arr)

    # todo: speed up
    # count = sort_arr.count(next_value)
    # if m==2:
    #     return count * cal_min_ops(diff)
    # # there are at least 3 diff values: min_v, next_value and next_next_value, thus we first need to
    # # convert min_v to next value
    # # assume the next value occur k times, then we need to do k conversions
    # k = count
    # idx = k + fix_idx
    # n_ops = k * cal_min_ops(diff)
    # new_arr = idx * [next_value] + [sort_arr[j] + k * diff for j in range(idx, n)]
    # return n_ops + equal(new_arr)


def cal_min_ops(diff):
    # in each operation, she can give x chocolates to some n-1 colleagues, where x in [1,2 or 5]
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
