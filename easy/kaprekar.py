#!/bin/python3


# Complete the kaprekarNumbers function below.
def isKaprekar(n):
    # n has d digits then n^2 has 2d or 2d-1 digits
    # split n^2 into left n right parts where right part r must have d digits
    # so r is simply n mod 10^d
    d = len(str(n))
    right = (n ** 2) % (10 ** d)
    left = (n ** 2) // (10 ** d)
    return left + right == n


def kaprekarNumbers(p, q):
    kap_nums = []
    for n in range(p, q + 1):
        if isKaprekar(n):
            kap_nums.append(n)

    if not kap_nums:
        print('INVALID RANGE')
    else:
        print(' '.join([str(n) for n in kap_nums]))


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
