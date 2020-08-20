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

    sort_arr = sorted(arr)
    return find_min_ops(sort_arr)


def find_min_ops(arr):
    # Given a sorted array arr, find the min number of ops needed to equalize all elements of a

    uniq_values = find_uniq_values(arr)
    m = len(uniq_values)
    # if all elements equal, do nothing
    if m == 1:
        return 0

    # Go backward, to absorb the max value instead
    #  if we absorb max_v to a smaller value, say v_i,
    # then the resulting dist will behave exactly as the initial dist with smaller values,
    # (because all smaller values are boosted same amount, so diff keep unchanged)
    # So, the min no. of ops when we absorb v_m to v_i is:
    # min_ops(arr drop all max_v) + count(max_v) * min_ops(max_v - v_i)
    # As the only term depending on i is min_ops(max_v - v_i), we only need to minimize that term
    max_v = uniq_values[-1]

    min_ops = min([cal_min_ops(max_v - uniq_values[i]) for i in range(m-1)])
    # drop all max_v from arr
    new_arr = [x for x in arr if x < max_v]
    return find_min_ops(new_arr) + arr.count(max_v) * min_ops

    # Work but slow
    # else, need to give chocolates to those with min number so that they can be equal with another group,
    # but not know which group is best, so try all

    # min_v = uniq_values[0]
    # n_min_ops = []
    # for v in uniq_values[1:]:
    #     # boost the group with min_v  to absorb the group with v bars, then repeat the process on new
    #     # dist of chocolates
    #     diff = v - min_v
    #     count_v = arr.count(v)
    #     n_ops = count_v * cal_min_ops(diff)
    #     # two groups with min_v and v are merged together
    #     # other groups are boosted by count(v) * diff
    #     boost_amt = count_v * diff
    #     new_arr = [min_v + boost_amt for w in arr if w in [min_v, v]] + \
    #               [w + boost_amt for w in arr if w not in [min_v, v]]
    #     n_min_ops.append(n_ops + find_min_ops(new_arr))
    # return min(n_min_ops)


def cal_min_ops(diff):
    # in each operation, she can give x chocolates to some n-1 colleagues, where x in [1,2 or 5]
    i = diff // 5
    r = diff % 5
    j = r // 2
    k = r % 2
    min_ops = i + j + k
    return min_ops


if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except PermissionError:
        test = int(input())
        folder = 'equal-testcases/output'
        fname = 'my_out_{}.txt'.format(test)
        fptr = open(os.path.join(folder, fname), 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
