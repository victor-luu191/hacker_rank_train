import math


def makeGrid(s, rows, columns):
    # Split s into a grid of rows, each row has columns

    # As s may have less than rows*columns chars, we pad missing chars with spaces
    n_miss = rows * columns - len(s)
    pad_s = ''.join([s, ' ' * n_miss])

    grid = []
    for r in range(rows):
        start = r * columns
        end = start + columns
        grid.append(pad_s[start:end])  # no fear of index out of range as we already do the padding

    return grid


def getColumn(c, grid):
    return [row[c] for row in grid]


def encode(grid):
    res = []
    # from each column of the grid, make a string from its entries and strip spaces from the string
    columns = len(grid[0])
    for c in range(columns):
        res.append(''.join(getColumn(c, grid)).rstrip())
    return ' '.join(res)


def calRowsColumns(L):
    # compute rows and columns of the grid
    side = math.sqrt(L)
    floor = math.floor(side)
    ceil = math.ceil(side)
    if floor == ceil:
        rows, columns = side, side
    else:
        if floor * ceil >= L:
            rows, columns = floor, ceil
        else:
            rows, columns = ceil, ceil

    return int(rows), int(columns)


def encryption(s):
    no_space_str = ''.join([c for c in s if c != ' '])
    L = len(no_space_str)
    rows, columns = calRowsColumns(L)
    print('rows: ', rows, ', columns: ', columns)
    # arrange chars to the grid of the rows, columns
    grid = makeGrid(no_space_str, rows, columns)
    return encode(grid)


if __name__ == '__main__':
    s = input('pls enter the string to be encoded \n')
    print(encryption(s))
