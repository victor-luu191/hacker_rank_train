import math


def solution(predicted, observed):
    # write your code in Python 3.6
    squares = []
    N = len(observed)
    for i in range(N):
        sq = (predicted[i] - observed[i])**2
        squares.append(sq)

    return math.sqrt(sum(squares)/N)