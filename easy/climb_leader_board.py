#!/bin/python3

import bisect
import os


# TODO: once we reach a list of unique decreasing scores, then the rank is simply index + 1,
#  thus no need to use a dict, a list is enough. So change to list for more opt
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


# As alice score keep climbing, if her current score already reach a certain rank
# then her next score should only be compared against people at higher ranks,
# ie. those beat her in current game.
# This will help us to skip redundant comparison. But note that it will also reduce
# size of the leader board, so need to handle edge case when lb empty.
def new_climbingLeaderboard(scores, alice):
    # first need to map each score in leader board to correct rank
    lb_ranks = assignRanks(scores)
    inc_scores = list(sorted(lb_ranks.keys()))
    # print(dec_scores)   # to check if scores already sorted decreasingly

    alice_ranks = []
    prev_index = 0  # play no game yet, so 0 score, thus should be put before all guys in leader board

    for s in alice:
        # find the first person beating Alice in current game, ie.,
        # return index k s.t. score[k] > s >= score[k+1].
        # To reduce redundant checks, we only compare against those beating her in prev game.
        current_index = bisect.bisect(inc_scores, s, lo=prev_index, hi=len(inc_scores))
        print('insert score ', s, ' at index ', current_index)

        if current_index >= len(inc_scores):    # no one beat Alice, so she take 1st rank
            current_rank = 1
        else:
            upper_score = inc_scores[current_index]
            current_rank = lb_ranks[upper_score] + 1

        print('score: ', s, ', current rank: ', current_rank)
        alice_ranks.append(current_rank)

        # prepare for next climb
        prev_index = current_index

    return alice_ranks


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = new_climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()



