#!/bin/python3


# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


if __name__ == '__main__':
    n = int(input())

    print(extraLongFactorials(n))
