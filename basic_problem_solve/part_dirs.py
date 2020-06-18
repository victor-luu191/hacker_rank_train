#!/bin/python3

import math
import os
import random
import re
import sys

class Node():
    def __init__(self, dd, file_size):
        self.dd = dd
        self.file_size = file_size




#
# Complete the 'mostBalancedPartition' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY parent
#  2. INTEGER_ARRAY files_size
#

def get_nodes(parent, files_size):
    pass


def make_tree(parent, files_size):
    pass


def cut_at_node(n, tree):
    pass


def c_size(tree):

    pass


def mostBalancedPartition(parent, files_size):
    # Write your code here
    nodes = get_nodes(parent, files_size)
    tree = make_tree(parent, files_size)

    min_diff = -1
    for n in nodes:
        left, right = cut_at_node(n, tree)
        diff = abs(c_size(left) - c_size(right))

        if diff < min_diff:
            min_diff = diff

    return min_diff



if __name__ == '__main__':
    # add code to handle input here

    result = mostBalancedPartition(parent, files_size)