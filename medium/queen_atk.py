#!/bin/python3

import os


def find_upper_part(r, c, lower_left_boundary, upper_right_boundary, diag):
    # stop when the cell hits upper OR left/right boundary (if diag=1/diag=2)
    upper_cell = [r + 1, c - 1]
    if diag == 1:
        if r == upper_right_boundary or c == lower_left_boundary:
            return []
        return [upper_cell] + find_upper_part(r + 1, c - 1, lower_left_boundary, upper_right_boundary, diag)
    if diag == 2:
        if r == upper_right_boundary or c == upper_right_boundary:
            return []
        return [upper_cell] + find_upper_part(r + 1, c - 1, lower_left_boundary, upper_right_boundary, diag)


def find_lower_part(r, c, lower_left_boundary, upper_right_boundary, diag):
    # stop when the cell hits lower boundary OR right/left boundary (if diag=1/diag=2)
    lower_cell = [r - 1, c + 1]
    if diag == 1:
        if r == lower_left_boundary or c == upper_right_boundary:
            return []
        return [lower_cell] + find_lower_part(r - 1, c + 1, lower_left_boundary, upper_right_boundary, diag)
    if diag == 2:
        if r == lower_left_boundary or c == lower_left_boundary:
            return []
        return [lower_cell] + find_lower_part(r - 1, c + 1, lower_left_boundary, upper_right_boundary, diag)


def find_cells_on_diag(r_q, c_q, lower_left_boundary, upper_right_boundary, diag=1):
    # given queen's position and board size,
    # return the first/second diag passing the queen

    # First main diag:
    # cases: queen above/below/on 1st main diag
    # above: queen 1st diag will touch upper (row=n) and right (col=n) boundaries,
    upper_part = find_upper_part(r_q, c_q, lower_left_boundary, upper_right_boundary, diag)
    lower_part = find_lower_part(r_q, c_q, lower_left_boundary, upper_right_boundary, diag)
    queen_cell = [r_q, c_q]
    queen_diag = upper_part + [queen_cell] + lower_part
    print('cells on queen diag', diag, ':')
    print(queen_diag)
    return queen_diag


def intersect(a1, a2):
    # given 2D arrays a1, a2, return their intersection
    return [e for e in a1 if e in a2]


def cal_cells_queen_attack_on_diag(r_q, obs_arr, diag_q):
    above_obstacle_rows = [obs[0] for obs in obs_arr if obs[0] > r_q]
    if above_obstacle_rows:
        upper_min = min(above_obstacle_rows)
    else:
        # if no obstace above queen, it can atk up to upper bound of its diag
        upper_min = max([cells[0] for cells in diag_q])

    below_obstacle_rows = [obs[0] for obs in obs_arr if obs[0] < r_q]
    if below_obstacle_rows:
        lower_max = max(below_obstacle_rows)
    else:
        lower_max = min([cells[0] for cells in diag_q])

    return upper_min - lower_max - 2  # exclude also the cell queen is on


def find_cells_queen_atk_on_diag(r_q, c_q, obstacles, n, diag=1):
    diag_of_queen = find_cells_on_diag(r_q, c_q, lower_left_boundary=1, upper_right_boundary=n, diag=diag)
    obstacles_on_diag_of_queen = intersect(obstacles, diag_of_queen)

    cells_queen_attack_on_diag = cal_cells_queen_attack_on_diag(r_q, obstacles_on_diag_of_queen, diag_of_queen)
    print('cells queen can atk on diag', diag, ':', cells_queen_attack_on_diag)
    return cells_queen_attack_on_diag


def find_column_cells_queen_attack(r_q, c_q, obstacles, bsize):
    obstacles_above_queen = [obs for obs in obstacles if obs[1] == c_q and obs[0] > r_q]
    obstacles_below_queen = [obs for obs in obstacles if obs[1] == c_q and obs[0] < r_q]
    if obstacles_above_queen:
        above_min = min([obs[0] for obs in obstacles_above_queen])
    else:
        above_min = bsize

    if obstacles_below_queen:
        below_max = max([obs[0] for obs in obstacles_below_queen])
    else:
        below_max = 1

    col_atks = above_min - 1 - below_max - 1  # exclude cell the queen is on
    print('cells queen can atk on its column:', col_atks)
    return col_atks


def find_row_cells_queen_attack(r_q, c_q, obstacles, bsize):
    obstacles_on_left_queen = [obs for obs in obstacles if obs[0] == r_q and obs[1] < c_q]
    obstacles_on_right_queen = [obs for obs in obstacles if obs[0] == r_q and obs[1] > c_q]
    # get column of closest_obstacle_on_left

    if obstacles_on_left_queen:
        left_max = max([obs[1] for obs in obstacles_on_left_queen])
    else:   # no obs, so can atk up to left boundary
        left_max = 1


    if obstacles_on_right_queen:
        right_min = min([obs[1] for obs in obstacles_on_right_queen])
    else: # no obs, so can atk up to right boundary
        right_min = bsize
    # cells queen can atk on row
    row_atks = right_min - 1 - left_max - 1  # exclude cell the queen is on
    print('cells queen can atk on its row:', row_atks)
    return row_atks


# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    # obstacles only block queen when they are on the atk paths,
    # any time we meet an obs, the regions, queen can atk is reduced
    # ROW:
    # the obs closest to the queen on her left will block on cells bf it,
    # the obs closest to the queen on her right will block on cells behind it
    # COL:
    # the obs closest to the queen above her block all cells above it
    # the obs closest to the queen below her block all cells below it
    # DIAG: similar

    # closest_obstacle_on_left = find_closest_obstacle_on_left(r_q, c_q, obstacles)

    # find cells queen can atk on its row
    row_atks = find_row_cells_queen_attack(r_q, c_q, obstacles, bsize=n)

    # find cells queen can atk on its column
    col_atks = find_column_cells_queen_attack(r_q, c_q, obstacles, bsize=n)

    # find cells queens can atk on its 1st diag
    first_diag_atks = find_cells_queen_atk_on_diag(r_q, c_q, obstacles, n, diag=1)

    # find cells queens can atk on its 2nd diag
    second_diag_atks = find_cells_queen_atk_on_diag(r_q, c_q, obstacles, n, diag=2)

    return row_atks + col_atks + first_diag_atks + second_diag_atks


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
