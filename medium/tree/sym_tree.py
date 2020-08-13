#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def find_paths(t):
    # given a binary tree, return all paths in t, each path represented as a binary str
    # add root as start of all paths, then move either left or right, depend on which side exists,
    # if left exists, find all left paths = [ '0' + p for p in paths in left sub tree]
    # right paths = ['1' + p for p in paths in right sub tree]

    # stop cond
    if not t:
        return []
    if (not t.left) and (not t.right) :
        return ['']

    left_paths = ['0' + p for p in find_paths(t.left)]
    right_paths = ['1' + p for p in find_paths(t.right)]
    paths = left_paths + right_paths
    return paths


def make_mirror_path(p):
    # given a path p represented as a binary str, return its mirror path by reversing its bits
    mp = ''.join([str(1 - int(b)) for b in p])
    return mp


def get_values(p, t):
    # return all values on path p of tree t
    # add root value to the list, then follow the correct side specified by p[0] to the next node,
    # repeat process
    if not p:   # no more edge, means we are at leaf node already
        if t:
            return [t.value]
        else:   # why there is this edge case?
            return []

    if p[0] == '0':
        return [t.value] + get_values(p[1:], t.left)
    if p[0] == '1':
        return [t.value] + get_values(p[1:], t.right)


def is_valid_path(bs, t):
    # given a tree t and a binary str representing a path, check if it is a valid path in t,
    # eg. it is a path from root to a leaf in t
    current = t

    # follow 0/1 in the str, if any move is invalid then return false
    for d in bs:
        if d == '0' and not current.left:
            return False
        if d == '0' and current.left:
            current = current.left
        if d == '1' and not current.right:
            return False
        if d == '1' and current.right:
            current = current.right

    # though we complete the whole str, if not reach a leaf yet then the str is not valid
    # as it stops in the middle of a path
    if (not current.left) and (not current.right):
        return True
    return False


def isTreeSymmetric(t):
    # symmetric around its center, i.e. each side mirrors the other.

    # a side is a path from root to leaf, and each edge is either left (0) or right (1), so each side
    # is a binary string.
    # symmetric side of a given side s can be obtained by reverse each bit in s.
    # For each side s on the left tree, check
    # symm cond = its symmetric side exists in tree and contains same values at the nodes with s.
    # i) if such condition is false, return false
    # ii) else, move on to the next side
    # If all edges satisfy the symmetric cond, return true

    paths = find_paths(t)
    print('paths in tree:', paths)
    left_paths = [p for p in paths if p.startswith('0')]
    right_paths = [p for p in paths if p.startswith('1')]
    if not left_paths:
        return not right_paths

    for lp in left_paths:
        rp = make_mirror_path(lp)
        # print('left path:', lp)
        # print('its mirror path:', rp)
        left_values = get_values(lp, t)
        right_values = get_values(rp, t)
        # print('left values:', left_values)
        # print('right values:', right_values)
        # todo: optimize the check if rp is a valid path

        # sym_cond = (rp in right_paths) and (left_values == right_values)
        sym_cond = is_valid_path(rp, t) and (left_values == right_values)
        if not sym_cond:
            return False
    return True
