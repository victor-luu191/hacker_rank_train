#!/bin/python3

import os


# Complete the dayOfProgrammer function below.
def find_month_contain_day(x, n_day):
    months = range(1, 13)
    for m in months:
        if sum([n_day[i] for i in range(1, m + 1)]) >= x:
            return m


def find_date_of_day(x, year, calendar):
    # idea: the month k in which 256th day falls in must satisfy:
    # total days of previous months < 256 <= totals days of months from 1 up to k

    # map each month to its number of days, handle feb depending on whether the year is leap yr
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    n_day = dict(zip(months_with_31_days, [31] * len(months_with_31_days)))

    months_with_30_days = [m for m in range(1, 13) if m not in months_with_31_days + [2]]
    d2 = dict(zip(months_with_30_days, [30] * len(months_with_30_days)))
    n_day.update(d2)

    # find number of days in feb
    n_day[2] = find_days_in_feb(year, calendar)

    # find month, given x
    mm = find_month_contain_day(x, n_day)

    # find date
    dd = x - sum([n_day[i] for i in range(1, mm)])

    return ".".join([str(dd).zfill(2), str(mm).zfill(2), str(year)])


def find_days_in_feb(year, calendar):
    if calendar == 'julian':
        if year % 4 == 0:
            days_in_feb = 29
        else:
            days_in_feb = 28
    if calendar == 'gregorian':
        if year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0):
            days_in_feb = 29
        else:
            days_in_feb = 28
    # 14th feb is 32nd day of year, so 14th feb is same as 1st feb in a normal yr
    # means feb only has 15 days
    if year == 1918:
        days_in_feb = 15
    return days_in_feb


def dayOfProgrammer(year):
    if year < 1918:
        return find_date_of_day(256, year, calendar='julian')
    if year > 1918:
        return find_date_of_day(256, year, calendar='gregorian')
    if year == 1918:
        return find_date_of_day(256, year, calendar='')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
