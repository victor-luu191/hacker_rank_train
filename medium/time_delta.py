# !/bin/python3
import calendar
import os
from calendar import monthrange
from collections import namedtuple
from datetime import datetime as dt


# Logic: the difference has the following components:
# i) day difference
#  ii) time difference: have to include time zone offsets from UTC

# When we compute time difference, we have to convert both times back to UTC ,
# so that we compare apple to apple.
# We do this conversion by adding/minus the offsets


def time_delta(t1, t2):
    # simple one, use built-in methods of datetime
    # format of timestamps: Day dd Mon yyyy hh:mm:ss +xxxx
    time1 = dt.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    time2 = dt.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    diff = time1 - time2
    print(diff)
    return diff.total_seconds()


# My own implementation without using built-in method from datetime library
def my_time_delta(t1, t2):
    # compute difference in days
    d1, d2 = get_date(t1), get_date(t2)
    day_diff = cal_day_diff(d1, d2)
    day_diff_in_hours = day_diff * 24
    day_diff_in_seconds = day_diff_in_hours * 3600
    print('day diff converted to seconds:', day_diff_in_seconds)

    # compute time difference in hours:mins:seconds
    time1, time2 = get_time(t1), get_time(t2)
    t1_in_utc = to_utc(time1)  # time elapsed since 00:00:00 to t1
    t2_in_utc = to_utc(time2)  # time elapsed since 00:00:00 to t2
    time_diff_in_seconds = t1_in_utc - t2_in_utc  # correct because in same day
    print('time diff in seconds:', time_diff_in_seconds)

    return time_diff_in_seconds + day_diff_in_seconds


Date = namedtuple('Date', 'dd mon yyyy')
Time = namedtuple('Time', ['hour', 'minute', 'second', 'offset'])
seconds_in_a_day = 24 * 60 * 60
seconds_in_a_hour = 3600
seconds_in_a_minute = 60


def get_date(date_time_str):
    # given a datetime string in format "Day dd Mon yyyy hh:mm:ss +xxxx",
    # return the date part as a named tuple (day, month, year), if namedtuple not avail then use a normal tuple
    # to extract date part, the simplest way is to split the time string by space,
    # then the first 4 sub-str forms date (more advanced is reg-exp, later)

    parts = str.split(date_time_str)
    day, dd, mon, yyyy = parts[0], parts[1], parts[2], parts[3]
    date = Date(dd=dd, mon=mon, yyyy=yyyy)
    return date


def get_time(date_time_str):
    # given a datetime string in format "Day dd Mon yyyy hh:mm:ss +xxxx",
    # return the time part as a named tuple (hour, minute, second, offset)
    parts = str.split(date_time_str)
    time_str = str.strip(parts[4])
    offset = str.strip(parts[5])
    time_parts = str.split(time_str, ':')
    hh, mm, ss = int(time_parts[0]), int(time_parts[1]), int(time_parts[2])

    time_with_offset = Time(hour=hh, minute=mm, second=ss, offset=offset)
    print('time:', time_with_offset)
    return time_with_offset


def to_month_number(mon_name):
    # given a month name in abbreviated format, eg. Jan, Feb, return the month number
    return {v: k for k, v in enumerate(calendar.month_abbr)}[mon_name]


def cal_elapsed(date: Date):
    # given a date, compute elapsed days between it and the first day of the same year
    # also handle edge cases of leap years

    dd, mon, yr = int(date.dd), to_month_number(date.mon), int(date.yyyy)
    n_day = dd
    for mm in range(1, mon):
        n_day += monthrange(yr, mm)[1]  # monthrange also handles leap year
    elapsed_days = n_day
    # print('elapsed days since 01-Jan of same year:', elapsed_days)
    return elapsed_days


def cal_day_diff_same_year(d1: Date, d2: Date) -> int:
    # given two dates d1 >= d2, return their difference in days

    # this version assumes that two dates are in the same year, then the difference is simply
    # duration between d1 and first day of the year - duration between d2 and first day of the year.

    elapsed_d1 = cal_elapsed(d1)
    elapsed_d2 = cal_elapsed(d2)
    diff_in_days = elapsed_d1 - elapsed_d2
    return diff_in_days


def get_days_in_year(yy):
    if not calendar.isleap(yy):
        return 365
    else:
        return 366


def year_range_to_days(start_year, end_year):
    # given a range from start year to end year, return number of days between them
    return sum([get_days_in_year(yy) for yy in range(start_year, end_year)])


def cal_day_diff(d1: Date, d2: Date) -> int:
    # if two dates are in different years, things get a bit more complicated.
    # Say d2 is in year2 (smaller year) and d1 is in year1, then the formula is like this:
    # cal_day_diff_same_year(end of year2, d2) + years_to_days(year2 + 1, year1) + cal_day_diff_same_year(d1, start of year1)

    year1, year2 = int(d1.yyyy), int(d2.yyyy)
    if year1 == year2:
        diff_in_days = cal_day_diff_same_year(d1, d2)
        print('diff in days:', diff_in_days)
        return diff_in_days

    if year1 > year2:
        end_of_year2 = Date(dd='31', mon='Dec', yyyy=str(year2))
        start_of_year1 = Date(dd='01', mon='Jan', yyyy=str(year1))
        duration1 = cal_day_diff_same_year(end_of_year2, d2)
        print('duration1:', duration1)
        duration2 = year_range_to_days(year2 + 1, year1)
        print('duration2:', duration2)
        duration3 = cal_day_diff_same_year(d1, start_of_year1)
        print('duration3:', duration3)
        diff_in_days = duration1 + duration2 + duration3 + 1
        print('diff in days:', diff_in_days)
        return diff_in_days


def cal_offset_amount(offset_str):
    # given an offset string of form hhmm, return offset amount in seconds
    hh, mm = int(offset_str[:2]), int(offset_str[2:])
    offset_amt_in_seconds = hh * seconds_in_a_hour + mm * seconds_in_a_minute
    print('offset amount in seconds:', offset_amt_in_seconds)
    return offset_amt_in_seconds


def to_utc(time: Time) -> int:
    # given a time, convert it to utc, then compute the time elapsed since 00:00:00 (of same day),
    # in number of seconds
    # return that time elapsed

    hh, mm, ss = time.hour, time.minute, time.second
    offset = time.offset

    elapsed_in_seconds = hh * seconds_in_a_hour + mm * seconds_in_a_minute + ss
    offset_sign = offset[0]
    offset_amt_in_seconds = cal_offset_amount(offset[1:])
    if offset_sign == '+':
        return elapsed_in_seconds - offset_amt_in_seconds
    else:
        return elapsed_in_seconds + offset_amt_in_seconds


# End of my own implementation

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

        my_delta = my_time_delta(t1, t2)

    fptr.close()
