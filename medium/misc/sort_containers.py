#!/bin/python3

import os


def getCounts(ls):
    counts = {}
    for x in ls:
        if x in counts.keys():
            counts[x] += 1
        else:
            counts[x] = 1

    return counts


def areSameMultisets(setA, setB):
    # two multisets are the same if i) they contain the same set of elements, and
    # ii) the elements have the same counts in both sets

    a_counts = getCounts(setA)
    b_counts = getCounts(setB)

    print('counts in multiset A: ', a_counts)
    print('counts in multiset B: ', b_counts)

    # check if a_counts and b_counts are the same
    for x in a_counts.keys():
        if x not in b_counts:
            return False
        else:
            if a_counts[x] != b_counts[x]:
                return False

    for y in b_counts.keys():
        if y not in a_counts.keys():
            return False
        else:
            if a_counts[y] != b_counts[y]:
                return False

    return True


# Complete the organizingContainers function below.
def organizingContainers(containers):
    # Ideas:
    # i) from def of containers matrix, entries in a column c are the numbers of balls of a certain color.
    # So sum of entries in a given column is the total number of balls of that color.
    # ii) swapping ball keep number of balls in a container unchanged. THUS,
    # it is possible to gather all balls of a given color c into a given container iff
    # the number of balls in that container equals to the number of balls of color/column c.
    # Assume the container is row r, this means the sum of row r entries equals to the sum of column c.
    # Conclusion: possible when the multiset of values of column sums is the same as the multiset of values of row sums
    # ie. if we have k columns each sums to C then we also must have exactly k rows each sums to C, for any C.

    # cal row sums
    row_sums = []
    for cc in containers:   # each container is a row
        row_sums.append(sum(cc))

    # cal column sums
    n_row = len(containers)
    n_col = n_row
    col_sums = []
    for col in range(n_col):
        col_sums.append(sum([containers[row][col] for row in range(n_row)]))

    if areSameMultisets(row_sums, col_sums):
        return "Possible"
    else:
        return "Impossible"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        containers = []

        for _ in range(n):
            containers.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(containers)
        fptr.write(result + '\n')

    fptr.close()
