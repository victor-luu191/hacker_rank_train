#!/bin/python3

import os


# Complete the maximumToys function below.
# Pre: prices are sorted increasingly
def maximumToys(prices, k):
    # we keep picking cheapest toys until their total exceeding amount
    total = 0
    n_toy = 0
    exceed = False
    while (not exceed) and (n_toy < len(prices)):
        # try adding
        total += prices[n_toy]
        exceed = (total > k)
        if not exceed:
            n_toy += 1

    return n_toy


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(sorted(prices), k)
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
