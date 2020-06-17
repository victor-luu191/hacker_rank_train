#!/bin/python3

import os

def assignRanks(scores):
    # map each score in leader board to correct rank
    # for that we will need to keep track of the lowest rank avail.
    ranks = {}
    ranks[scores[0]] = 1
    lowest_rank = 1
    for s in scores[1:]:
        if s not in ranks.keys():  # meet a new lower score, thus assign lower rank
            lowest_rank += 1
            ranks[s] = lowest_rank

    return ranks


# perform a linear search to find correct rank of given score
def linearRank(s, dec_scores):
    n = len(dec_scores)
    if n == 0:  # empty leaderboard, no competitor, thus take 1st place
        return 1
    else:
        # among the dec_scores, find the 1st score larger than given score s,
        # then the rank of s should be right after then the rank of the found score
        found = False
        i = n
        while not found:
            i -= 1
            found = (dec_scores[i] > s)
        # always can find a larger score as there is an inf score in the score list
        return i + 1


# a binary search to exploit the fact that lb scores are already sorted
# return index of the first guy with score larger than given score s, ie. return k s.t. score[k] > s >= score[k+1]
def binarySearch(s, dec_scores):
    n = len(dec_scores)
    # Stop condition
    if n == 0:  # leader board is empty, thus no guy beat Alice
        return 0
    else:
        first, last = 0, n - 1
        mid = (first + last) // 2
        print('first: ', first, ', last: ', last, ', mid: ', mid)
        if s > dec_scores[mid]:  # then s must be at some index from mid - 1 bkward to start
            index = binarySearch(s, dec_scores[:mid])
            # debug
            # print('comparing against scores: ', dec_scores[:mid])
            # print('score: ', s, ', has index: ', index)
            return index
        if s < dec_scores[mid]:  # then s must be at some index from mid + 1 to end
            scores_to_compare = dec_scores[mid + 1:]
            index_after_mid = binarySearch(s, scores_to_compare)
            index = mid + 1 + index_after_mid
            # debug
            # print('comparing against the scores after position ', mid, ' : ', scores_to_compare)
            # print('score: ', s, ' has index: ', index_after_mid)
            # print('thus, its final index is: ', index)
            return index

        if s == dec_scores[mid]:
            index = mid
            return index

# the method below works but not optimized as we do the search again for each new score of Alice
def old_climbingLeaderboard(scores, alice):
    # first need to map each score in leader board to correct rank
    lb_ranks = assignRanks(scores)
    # check if scores in rank dict already sorted
    for item in lb_ranks.items():
        print(item)

    # find correct position to insert each Alice score
    alice_ranks = []
    for s in alice:
        alice_ranks.append(linearRank(s, dec_scores=lb_ranks.keys()))

    return alice_ranks