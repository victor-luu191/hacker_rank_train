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
    # i) if arr only contains two groups with v and v+d bars, then we just keep boosting guys with
    # less bars until all equals, then will need min_ops(d) * count(v+d).
    # process: fix a guy wit v+d bars,
    # boost all guys with v bars to v+d, then other guys with v+d bars, if have, will get v+2d bars.
    # So the diff continue to be d and we can repeat the process, this time with one less inequal.
    # repeat until all larger guys are absorbed, there are count(v+d), so totally count(v+d) * min_ops(d)
    # ii) if more than 2 groups, then start with the group with min bars, boost it to reach some other group,
    # then the number of groups will be reduced by 1 and we can continue until there is only 1 group,
    # ie. all equal

    uniq_values = sorted(find_uniq_values(arr))
    min_v = uniq_values[0]
    m = len(uniq_values)
    # if all elements equal, do nothing
    if m == 1:
        return 0

    # else, need to give chocolates to those with min number so that they can be equal with another group,
    # but not know which group is best, so try all
    n_min_ops = []
    for v in uniq_values[1:]:
        # boost the group with min_v  to absorb the group with v bars, then repeat the process on new
        # dist of chocolates
        diff = v - min_v
        count_v = arr.count(v)
        n_ops = count_v * cal_min_ops(diff)
        # two groups with min_v and v are merged together
        # other groups are boosted by count(v) * diff
        boost_amt = count_v * diff
        new_arr = [min_v + boost_amt for w in arr if w in [min_v, v]] + \
                  [w + boost_amt for w in arr if w not in [min_v, v]]
        n_min_ops.append(n_ops + equal(new_arr))
    return min(n_min_ops)


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
