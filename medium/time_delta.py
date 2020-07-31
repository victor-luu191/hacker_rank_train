# !/bin/python3

import math
import os
import random
import re
import sys
from collections import namedtuple
from datetime import datetime as dt

# Logic: the difference has the following components:
# i) day difference
#  ii) time difference: have to include time zone offsets from UTC

# When we compute time difference, we have to convert both times back to UTC ,
# so that we compare apple to apple.
# We do this conversion by adding/minus the offsets

Date = namedtuple('Date', 'dd mon yyyy')
Time = namedtuple('Time', ['hour', 'minute', 'second', 'offset'])


def get_date(time_str):
    # given a time string in format "Day dd Mon yyyy hh:mm:ss +xxxx",
    # return the date part as a named tuple (day, month, year), if namedtuple not avail then use a normal tuple
    # to extract date part, the simplest way is to split the time string by space,
    # then the first 4 sub-str forms date (more advanced is reg-exp, later)

    parts = str.split(time_str)
    day, dd, mon, yyyy = parts[0], parts[1], parts[2], parts[3]
    date = dt.strptime('-'.join([dd, mon, yyyy]), '%d-%b-%Y')

    print('date:', date)
    return date
    # return Date(dd=dd, mon=mon, yyyy=yyyy)


def cal_day_diff(d1, d2):
    # given two dates, return their difference in days (can use datetime methods?)

    pass


def to_utc(time):
    pass


def get_time(time_str):
    # given a time string in format "Day dd Mon yyyy hh:mm:ss +xxxx",
    # return the time part as a named tuple (hour, minute, second)
    pass


def cal_time_diff(t1_in_utc, t2_in_utc):
    # compute time difference in hours:mins:seconds
    pass


def to_seconds(time_diff):
    pass


seconds_in_a_day = 24 * 60 * 60


def time_delta(t1, t2):
    # simple one, use built-in methods of datetime
    # format of timestamps: Day dd Mon yyyy hh:mm:ss +xxxx
    time1 = dt.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    time2 = dt.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    diff = time1 - time2
    print(diff)
    return diff.total_seconds()
    # return diff.days * seconds_in_a_day  +

    # compute difference in days
    # d1, d2 = get_date(t1), get_date(t2)
    # day_diff = cal_day_diff(d1, d2)
    # day_diff_in_hours = day_diff * 24
    # day_diff_in_seconds = day_diff_in_hours * 3600

    # compute time difference in hours:mins:seconds
    # time1, time2 = get_time(t1), get_time(t2)
    # t1_in_utc = to_utc(time1)
    # t2_in_utc = to_utc(time2)
    # time_diff = cal_time_diff(t1_in_utc, t2_in_utc)
    # time_diff_in_seconds = to_seconds(time_diff)

    # return time_diff_in_seconds + day_diff_in_seconds


if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except PermissionError:
        fptr = open('time_delta_out.txt', 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(str(delta) + '\n')

    fptr.close()
