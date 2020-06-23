#!/bin/python3

import os
import re


def find_start_non_plus(s):
    for i in range(len(s)):
        if s[i] != '+':
            return i
    return None


def find_non_plus_ranges(s):
    # return start and stop of the block of non-plus chars (i.e !='+')
    # find index of the first non-plus letter
    start = find_start_non_plus(s)
    if start:
        stop = len(s) - find_start_non_plus(s[::-1])
        return start, stop
    else:
        return None, None


# todo: use re.finditer() for this method
def find_fillable_ranges(index, grid, axis=0):
    # given position in a grid and a direction (axis),
    # return content and positions of fillable range

    # a range is a string with chars in [-, a-z], pattern "-* | [a-z]*"
    # positions must contain index of row/column and start/stop of usable cells
    if axis == 0:
        print('\t finding fillable ranges in row', index)
        cells = grid[index]
    else:
        print('\t finding fillable ranges in column', index)
        cells = ''.join([grid[rr][index] for rr in range(len(grid))])

    fillable_ranges = re.finditer("[-a-z]", cells)    # this one is still wrong
    for m in fillable_ranges:
        print(m.start(), '-', m.end(), m.group(0))

    return fillable_ranges


# todo: modify this method to align with format of a range
def fill_word_into_position(wrd, a_range, grid, axis=0):
    # fill given word into given pos in given grid
    # return grid filled with the word

    index = a_range['index']
    start, end = a_range.start() , a_range.end()

    filled_grid = grid.copy()
    if axis == 0:  # fill into row
        filled_grid[index][start:end] = wrd
    else:  # fill to column
        for rr in a_range(start, end):
            filled_grid[rr][index] = wrd[rr - start]

    return filled_grid


def is_match(wrd, cells):
    # len match
    if len(cells) != len(words):
        print('len of word and usable cells not match')
        return False
    # letter match: filled letters in the cells must match letters at the same positions in wrd
    for i in range(len(cells)):
        if cells[i] != '-':
            if cells[i] != wrd[i]:
                print('letters at', i, 'positon of word and cells not match')
                return False
    print('word and usable cells MATCH!')
    return True


def try_filling(wrd, pos, grid, axis=0):  # axis 0 means row, 1 means col
    # a word can only be filled to a row/column (pos) if
    # i) len match: its length matches the no. of usable cells in pos
    # ii) letter match: its letters match with fixed letters in the row/column

    fillable_ranges = find_fillable_ranges(pos, grid, axis)
    for rr in fillable_ranges:
        if is_match(wrd, rr):  # word and the range match, so can fit
            filled_grid = fill_word_into_position(wrd, rr, grid, axis)
            print(filled_grid)
            return filled_grid
        else:
            return None

    pass


def crosswordPuzzle(grid, words):
    # Ideas:
    # 1. seem that each row only has 1 word
    # just try putting a proper word into the first line possible,
    # then try to put remain words into remain grid, on condition that
    # certain cells have fixed chars
    # this will finally lead to when only 1 row/column and 1 word left (stop cond)
    # so just need to check if the word can be fit to the row.
    # If the word cannot be fitted, then sth wrong and need to backtrack

    # STOP COND
    if len(words) == 0:
        return grid
    # =================================================

    # the first word must go some where in grid,
    # so try filling it into rows first, then try columns later
    # todo: (optimize) just jump to places where we can fit the  word
    w0 = words[0]

    n_row, n_cols = len(grid), len(grid[0])
    # try rows first
    for rr in range(n_row):
        grid_filled_with_the_word = try_filling(w0, rr, grid, axis=0)
        if grid_filled_with_the_word:  # successful fill
            res = crosswordPuzzle(grid_filled_with_the_word, words[1:])
            if res:
                return res

    # try filling into cols
    for cc in range(n_cols):
        grid_filled_with_the_word = try_filling(w0, cc, grid, axis=1)
        if grid_filled_with_the_word:  # successful fill
            res = crosswordPuzzle(grid_filled_with_the_word, words[1:])
            if res:
                return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
