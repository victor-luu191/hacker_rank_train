#!/bin/python3

import os


#
# Complete the 'receivedText' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING S as parameter.
#

def receivedText(s):
    # s contains Latin letters, underscores, digits, and four special characters
    # the bugs with the kb will make the cursor jump around in the resulting string,
    # so we need to keep track of its position to add chars in correct position.

    special_chars = ['<', '>', '*', '#']
    res = []
    cursor_pos = 0
    n_numlock_pressed = 0
    is_numlock_on = True
    for i in range(len(s)):
        # handle special chars
        if s[i] == '*':
            res = del_char_bf_cursor(cursor_pos, res)
        if s[i] == '>':  # move to end of res string to prep for adding chars from there (later)
            cursor_pos = len(res)
        if s[i] == '<':  # move to start of res string
            cursor_pos = 0
        if s[i] == '#':
            n_numlock_pressed += 1
            if n_numlock_pressed % 2 == 0:
                is_numlock_on = True
            else:
                is_numlock_on = False

        if (s[i] not in special_chars) and not s[i].isdigit():  # insert normally
            res.insert(cursor_pos, s[i])
            cursor_pos += 1
        # numlock funciton is reversed
        if s[i].isdigit() and is_numlock_on:
            res.insert(cursor_pos, s[i])
            cursor_pos += 1
        if s[i].isdigit() and not is_numlock_on: # cannot use any number, so just skip it
            pass

    return ''.join(res)


def del_char_bf_cursor(cursor_pos, s):
    if cursor_pos == 0:  # at start of string s
        pass
    else:  # delete prev char if have
        if len(s) > 0:
            prev_char = s[cursor_pos - 1]
            s.remove(prev_char)
        return s

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open("new_kb_out.txt", 'w')

    S = input()

    result = receivedText(S)

    fptr.write(result + '\n')

    fptr.close()
