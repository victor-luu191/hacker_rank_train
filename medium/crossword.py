#!/bin/python3

import os
import re


def find_fillable_ranges(axis, index, grid):
    # given position in a grid and a direction (axis),
    # return content and positions of fillable range

    # a range is a string with chars in [-, a-z], pattern "-* | [a-z]*"
    # positions must contain index of row/column and start/stop of usable cells
    if axis == 0:
        # print('\t finding fillable ranges in row', index)
        cells = grid[index]
    else:
        # print('\t finding fillable ranges in column', index)
        n_row = len(grid)
        cells = ''.join([grid[rr][index] for rr in range(n_row)])

    fillable_ranges = re.finditer("[^\+]+", ''.join(cells))
    return fillable_ranges


def fill_word_into_position(wrd, index, grid, a_range, axis=0):
    # fill given word into given pos in given grid
    # return grid filled with the word

    start, end = a_range.start(), a_range.end()

    filled_grid = grid.copy()
    if axis == 0:  # fill into row
        for cc in range(start, end):
            filled_grid[index][cc] = wrd[cc - start]
    else:  # fill to column
        for rr in range(start, end):
            filled_grid[rr][index] = wrd[rr - start]

    return filled_grid


def is_match(wrd, cells):
    # len match
    if len(cells) != len(wrd):
        # print('\t len of word and fillable range not match')
        return False
    # letter match: filled letters in the cells must match letters at the same positions in wrd
    for i in range(len(cells)):
        if cells[i] != '-':
            if cells[i] != wrd[i]:
                # print('letters at', i, 'position of word and cells not match')
                return False
    print('\t found a matching range for word ', wrd, '! Filling the word into the range')
    return True


def make_crossword(grid):
    # return crossword format from a 2d grid
    row_strings = [''.join(rr) for rr in grid]
    return '\n'.join(row_strings)


def try_filling(wrd, index, grid, axis=0):  # axis 0 means row, 1 means col
    # a word can only be filled to a row/column (pos) if
    # i) len match: its length matches the no. of usable cells in pos
    # ii) letter match: its letters match with fixed letters in the row/column

    fillable_ranges = find_fillable_ranges(axis, index, grid)
    if not fillable_ranges:
        pass

    for a_range in fillable_ranges:
        content = a_range.group(0)
        # print('range to fit, start:', a_range.start(), 'end:', a_range.end(),
        #       'content: ', content
        #       )
        if is_match(wrd, content):  # word and the (partial filled) content match, so can fit
            filled_grid = fill_word_into_position(wrd, index, grid, a_range, axis)
            print(make_crossword(filled_grid))
            return filled_grid
        else:
            return None


# todo: need to handle backtrack correctly
def crosswordPuzzle(grid, word_ls):
    # Ideas:
    # 1. seem that each row only has 1 word
    # just try putting a proper word into the first line possible,
    # then try to put remain words into remain grid, on condition that
    # certain cells have fixed chars
    # this will finally lead to when only 1 row/column and 1 word left (stop cond)
    # so just need to check if the word can be fit to the row.
    # If the word cannot be fitted, then sth wrong and need to backtrack

    # STOP COND
    if len(word_ls) == 0:
        return grid
    # =================================================

    # the first word must go some where in grid,
    # so try filling it into rows first, then try columns later
    # todo: (optimize) just jump to places where we can fit the  word
    w0 = word_ls[0]
    n_row, n_col = len(grid), len(grid[0])
    # try rows first
    print('Try filling word ', w0, ' into rows:')
    for rr in range(n_row):
        grid_filled_with_the_word = try_filling(w0, rr, grid, axis=0)
        if grid_filled_with_the_word:  # successful fill
            res = crosswordPuzzle(grid_filled_with_the_word, word_ls[1:])
            if res:
                return res

    # try filling into cols
    print('Filling word ', w0, ' into rows is wrong. Now try filling it into columns:')
    for cc in range(n_col):
        grid_filled_with_the_word = try_filling(w0, cc, grid, axis=1)
        if grid_filled_with_the_word:  # successful fill
            res = crosswordPuzzle(grid_filled_with_the_word, word_ls[1:])
            if res:
                return res

    # if all fail
    print('cannot fill word ', w0, ', back tracking')

    # need some way to recover grid to state before filling the word
    print('crossword at backtrack time:')

    pass


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open("xword_output1.txt", 'w')

    crossword = []

    for _ in range(10):
        crossword_item = list(input())
        crossword.append(crossword_item)

    words = input().split(';')

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
