#!/bin/python3

import os


def find_uniq_values(arr):
    uniq_values = []
    for v in arr:
        if v not in uniq_values:
            uniq_values.append(v)
    return uniq_values


def find_counts(sort_arr):
    # given a sorted array, return counts of elements in in
    uniq_values = find_uniq_values(sort_arr)
    return {v: sort_arr.count(v) for v in uniq_values}


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

    count = find_counts(sorted(arr))
    return find_min_ops(count)


def find_min_ops(count):
    # Given a distribution represent as a dict {v: count(v)}_v
    # find the min number of ops needed to equalize all elements of dist

    values = list(count.keys())
    m = len(values)
    # if all elements equal, do nothing
    if m == 1:
        return 0

    # Go backward, to absorb the max value instead
    #  if we absorb max_v to a smaller value, say v_i,
    # then the resulting dist will behave exactly as the initial dist with smaller values,
    # (because all smaller values are boosted same amount, so diff keep unchanged)
    # So, the min no. of ops when we absorb v_m to v_i is:
    # min_ops(new arr with max_v absorbed to v_i) + count(max_v) * min_ops(max_v - v_i)
    # two terms depending on i: min_ops(max_v - v_i), and new count of v_i in new array
    max_v = values[-1]
    count_max_v_ = count[max_v]
    n_min_ops = []
    for i in range(m - 1):
        min_ops_i =  count_max_v_ * cal_min_ops(max_v - values[i])

        # absorb all max_v into v_i, thus update counts and drop max_v
        new_count = dict(zip(count.keys(), count.values()))
        new_count[values[i]] += count_max_v_
        new_count.pop(max_v)
        print('new counts:', new_count)

        min_ops_i += find_min_ops(new_count)

        n_min_ops.append(min_ops_i)

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
