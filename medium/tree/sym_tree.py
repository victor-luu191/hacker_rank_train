#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def find_side(b, t):
    # given a tree t and a boolean b, return the (values on) left-most (b=0) or right-most (b=1) side of t,
    # starting from root
    if b == 0:  # always follow left until terminal
        # stop cond
        if not t.left:  # t is leaf already
            return [t]
        left_most_side = [t] + find_side(b, t.left)
        print('values on left most side:', get_values(left_most_side))
        return left_most_side
    else:
        if not t.right:
            return [t]
        right_most_side = [t] + find_side(b, t.right)
        print('values on right most side:', get_values(right_most_side))
        return right_most_side


def is_equal(side1, side2):
    # check if resp values on two sides are equal
    values1 = get_values(side1)
    values2 = get_values(side2)
    return values1 == values2


def get_values(side):
    return [n.value for n in side]


def isTreeSymmetric(t):
    # symmetric around its center, i.e. each side mirrors the other.

    # Recursive
    # get the left-most side, by always go left until reach leaf node
    # get the right-most side (sym side)
    # If left-most == right-most:
    # prune only leaf nodes from the tree, switch left --> right (things get ugly here)
    # and repeat checking
    # else: return false

    # stop cond
    if not t:
        return True

    left_most_side = find_side(0, t)
    right_most_side = find_side(1, t)
    if not is_equal(left_most_side, right_most_side) :
        return False
    # prune leaf nodes & continue checking
    left_most_side[-1] = None
    right_most_side[-1] = None
    # print('tree after pruning leaf nodes:')
    # print_tree(t)
    return isTreeSymmetric(t)
