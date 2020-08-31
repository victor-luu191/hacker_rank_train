import os
import pandas as pd
import numpy as np

arr = range(10)


def pop_idx(i, arr: list):
    return arr.pop(i)


def pop(arr: list):
    return arr.pop()


def my_pop(arr):
    last = arr[-1]
    arr = arr[:-1]
    return last


if __name__ == '__main__':
    a = list(range(10))
    # popped = [pop_idx(i, a) for i in range(5)]
    popped = [pop(a) for i in range(5)]
    print('popped values:', popped)
    print(a)
