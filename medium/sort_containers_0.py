#!/bin/python3

import os


def swapBalls(i, container):
    # given i!=0,
    # swap balls i in bin 0 with balls 0 in other bins, until no more balls i in bin 0
    # return a new matrix of bins after swapping

    swapped_container = container.copy()
    for j in range(1, len(container)):
        if swapped_container[0][i] == 0:
            print('after swapping out all balls ', i, ', resulting containers are: ', swapped_container)
            return swapped_container
        else:
            # if number of balls 0 in container j < number of balls i in container 0, swap all balls 0 in j
            if swapped_container[j][0] < swapped_container[0][i]:
                n_to_swap = swapped_container[j][0]
            else:  # swap all balls i out, balls 0 in
                n_to_swap = swapped_container[0][i]

            swapped_container[0][0] += n_to_swap
            swapped_container[0][i] -= n_to_swap
            swapped_container[j][0] -= n_to_swap
            swapped_container[j][i] += n_to_swap

    print('after swapping out all balls ', i, ', resulting containers are: ', swapped_container)
    return swapped_container


def isPossible(container):
    # possible = each container i contains all balls of that type i and only those balls
    # container: a two dimensional array of integers that represent the number of balls of each color in each container
    # if only 2 bins, then possible if number of balls misplaced in each container is the same, ie. n[0][1] = n[1][0]
    # more than 2 bins:
    # bins 0 have misplaced balls m[0][1], ..., m[0][n-1]
    # need to move all the misplaced balls from bin 0, and all balls 0 misplaced in other bins,
    # which is possible when the number of misplaced balls in bin 0 equals to the number of ball 0 misplaced in other bins
    # because we just keep swapping a ball i in bin 0 with ball 0 in another bin

    # stop condition
    # TODO: a better one is when len(container)==0, ie. no more bins to check, return true
    if len(container) == 2:
        return container[0][1] == container[1][0]

    # find total number of ball 0 in other bins, ie. bins[1:]
    total_0 = 0
    n_container, n_ball = len(container), len(container)
    for i in range(1, n_container):
        total_0 += container[i][0]

    n_misplaced_balls_in_bin0 = sum(container[0][1:])
    if total_0 == n_misplaced_balls_in_bin0:
        # keep swapping misplaced balls in bin 0 with balls 0 in other bins
        swapped_container = container.copy()
        for i in range(1, n_ball):
            swapped_container = swapBalls(i, swapped_container)
        #     successfully swap for container 0, only need to check remaning containers
        swapped_container_drop_first_row_col = []
        for i in range(1, n_container):
            swapped_container_drop_first_row_col.append(swapped_container[i][1:])
        return isPossible(swapped_container_drop_first_row_col)
    else:
        return False


# Complete the organizingContainers function below.
def organizingContainers(container):
    if isPossible(container):
        return 'Possible'
    return 'Impossible'


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)
        print(result + '\n')
        # fptr.write(result + '\n')

    # fptr.close()
