#!/bin/python3

import os



def find_start_non_plus(s):
    for i in range(len(s)):
        if s[i] != '+':
            return i
    return None

# todo: use re.findall() for this method
def find_non_plus_ranges(s):
    # return start and stop of the block of non-plus chars (i.e !='+')
    # find index of the first non-plus letter
    start = find_start_non_plus(s)
    if start:
        stop = len(s) - find_start_non_plus(s[::-1])
        return start, stop
    else:
        return None, None


def find_usable_cells(index, grid, axis=0):
    # given position in a grid and a direction (axis),
    # return content and positions of usable cells.

    # usable cells are not + (either marked with - or some alphabet)
    # positions must contain index of row/column and start/stop of usable cells
    if axis == 0:
        print('\t finding usable cells in row', index)
        row = grid[index]
        start, stop = find_non_plus_ranges(row)
        if start and stop:
            content = row[start:stop]
        else:
            content = None
    else:
        print('\t finding usable cells in column', index)
        col = ''.join([grid[rr][index] for rr in range(len(grid))])
        start, stop = find_non_plus_ranges(col)
        if start and stop:
            content = col[start: stop]
        else:
            content = None

    positions = {'index': index, 'start': start, 'stop': stop}
    if content:
        print('letters in usable cells: ', content)
        print('position of usable cells: ', positions)
        return content, positions


def fill_word_into_position(wrd, positions_of_cells, grid, axis=0):
    # fill given word into given pos in given grid
    # return grid filled with the word

    index = positions_of_cells['index']
    start, stop = positions_of_cells['start'], positions_of_cells['stop']

    filled_grid = grid.copy()
    if axis == 0:  # fill into row
        filled_grid[index][start:stop] = wrd
    else:  # fill to column
        for rr in range(start, stop):
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

    usable_cells, positions_of_cells = find_usable_cells(pos, grid, axis)
    if usable_cells:
        if is_match(wrd, usable_cells):  # word and the usable cells match, so can fit
            filled_grid = fill_word_into_position(wrd, pos, grid, axis)
            print(filled_grid)
            return filled_grid
        else:
            return None
    else:
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
