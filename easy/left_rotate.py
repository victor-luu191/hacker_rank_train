#!/bin/python3

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    left_a = a[d:] + a[0:d]
    print(' '.join([str(x) for x in left_a]))
