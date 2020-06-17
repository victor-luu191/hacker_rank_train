#!/bin/python3

import os


# Complete the luckBalance function below.
def luckBalance(k, contests):
    # lose more can boost luck more, thus should lose amap. so she can lose k important contests and
    # for non-imp can lose all

    # luck got from losing all non-imp
    non_imp_sum = sum([contests[i][0] for i in range(len(contests)) if contests[i][-1] == 0])

    # choose to lose k important contests with highest luck
    imp_lucks = [contests[i][0] for i in range(len(contests)) if contests[i][-1] == 1]
    sorted_imp_lucks = sorted(imp_lucks, reverse=True)
    k_best = sorted_imp_lucks[:k]
    best_gain_imp = sum(k_best)

    # must win all remain imp contests, thus lose some luck
    loss_imp = sum(sorted_imp_lucks[k:])

    return best_gain_imp + non_imp_sum - loss_imp


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
