# !/bin/python3

import os
from collections import deque

WEIGHT = 6


def find_neighbors(v, edges):
    # given adjacency matrix edges and a vertex v, return v's neighbors, eg. w's which (v, w) is an edge
    neighbors = []
    for e in edges:
        if v in e:
            if v == e[0]:
                neighbors.append(e[1])
            else:
                neighbors.append(e[0])
    print('neighbors of node', v, ':', neighbors)
    return neighbors


def lookup_dist(v, distances):
    if v in distances.keys():
        return distances[v]
    else:
        return -1


def bfs(n, m, edges, s):
    # For bfs, we need to use a queue and a fast implementation of queue in python is
    # via collections.deque, with O(1) append and popleft

    # Example:
    # pop s from the queue, visit s to get its n_hop (=0)
    # i) find all neighbors of s: N(s) = (n1, n2,..., nk)
    # ii) for each t in N(s): update n_hop(t) = n_hop(s) + 1
    # iii) add t's to the queue
    # Now queue = N(s)
    # pop an item t in queue, visit it to get t's n_hop value,
    # i) find t's neighbors N(t)
    # ii) for each u in N(t): update n_hop(u) = n_hop(t) + 1, but only if n_hop(u) is unknown
    # iii) add u's to the queue

    queue = deque()
    queue.append(s)
    # keep track of which vertices already added to the queue thus processed
    vertices = [i+1 for i in range(n)]
    values = [False] * n
    processed = dict(zip(vertices, values))

    #  a dict to keep track of n_hop at each level
    n_hop = dict()
    n_hop[s] = 0

    while queue:
        r = queue.popleft()
        n_hop_r_ = n_hop[r]  # visit r
        processed[r] = True
        neighbors = find_neighbors(r, edges)
        for t in neighbors:
            # if t not in n_hop.keys():
            if not processed[t] :  # t not added to queue yet, so it is not in any level above, so it is indeed at next level
                queue.append(t)
                processed[t] = True
                n_hop[t] = n_hop_r_ + 1

    # return distances
    distances = {v: (n_hop[v] * WEIGHT) for v in n_hop.keys()}
    print('distances:', distances)
    sort_distances = {v: lookup_dist(v, distances) for v in vertices}
    sort_distances.pop(s, None)
    return sort_distances.values()


if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except  PermissionError:
        out_dir = 'out'
        fptr = open(os.path.join(out_dir, 'bfs_00.txt'), 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
