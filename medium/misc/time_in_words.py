#!/bin/python3

import os


# Complete the timeInWords function below.
def mapHourToWord(h):
    hour_to_word = mapUnitsToWords()
    hour_to_word[10] = 'ten'
    hour_to_word[11] = 'eleven'
    hour_to_word[12] = 'twelve'
    hour_to_word[13] = 'one'
    return hour_to_word[h]


def mapUnitsToWords():
    units = range(0, 10)
    unit_words = ["", 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    unit_to_word = dict(zip(units, unit_words))
    return unit_to_word


def toWord(x):
    tenth_digit = x//10
    unit = x%10

    tens = range(2, 6)
    ten_words = ['twenty', 'thirty', 'forty', 'fifty']
    ten_to_word = dict(zip(tens, ten_words))
    return ' '.join([ten_to_word[tenth_digit], mapUnitsToWords()[unit]])


def mapMinutesToWord(m):
    minute_to_word = mapUnitsToWords()
    # 2-digit minutes

    minute_to_word[10] = 'ten'
    minute_to_word[11] = 'eleven'
    minute_to_word[12] = 'twelve'

    # teen minutes from 13 to 19, exclude 15
    teens = range(13, 20)
    teen_words = ["".join([p, "teen"]) for p in ['thir', 'four', 'fif', 'six', 'seven', 'eight', 'nine']]
    teen_dict = dict(zip(teens, teen_words))
    minute_to_word.update(teen_dict)

    # minutes >= 20, exclude 30
    ty_mins = range(20, 60)
    ty_words = [toWord(r) for r in ty_mins]
    ty_dict = dict(zip(ty_mins, ty_words))
    minute_to_word.update(ty_dict)

    # add " minutes "
    for k in minute_to_word.keys():
        minute_to_word[k] = ' '.join([minute_to_word[k], "minutes"])

    # special cases
    minute_to_word[15] = 'quarter'
    minute_to_word[30] = 'half'
    minute_to_word[1] = "one minute"

    return minute_to_word[m]


def timeInWords(h, m):
    if m == 0:
        return " ".join([mapHourToWord(h), "o' clock"])
    else:
        if m <= 30:
            return ' '.join([mapMinutesToWord(m), "past", mapHourToWord(h)])
        else:
            return ' '.join([mapMinutesToWord(60 - m), "to", mapHourToWord(h+1)])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
