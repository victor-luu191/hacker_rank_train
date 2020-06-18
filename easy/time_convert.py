#!/bin/python3

import os


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # if pm then add hh with 12, except edge case when hh is 12

    # get am/pm part
    is_pm = (s[-2:] == 'PM')
    hh_mm_ss = s[:-2].split(':')
    hh, mm, ss = hh_mm_ss[0], hh_mm_ss[1], hh_mm_ss[2]

    hh_amt = int(hh)
    if is_pm and hh_amt < 12:
        return ':'.join([str(hh_amt + 12), mm, ss])
    if is_pm and hh_amt == 12:  # noon
        return ':'.join(hh_mm_ss)

    # AM
    if not is_pm and (hh_amt == 12):  # midnight
        return ':'.join(['00', mm, ss])
    if not is_pm and hh_amt < 12:
        return ':'.join(hh_mm_ss)


if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)

    # f.write(result + '\n')
    #
    # f.close()
