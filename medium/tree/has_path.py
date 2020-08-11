#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(t, s):
    # assume that such a path p exists
    # start at root t, as t.value + sum(remaining part of p) = s, so sum(remaining part of p) = s - root.value. As remaining part of p is in either left sub tree or right sub tree,
    #  either of the sub tree should have such a path --> recursive.
    #
    # stop when nothing more
    if not t:
        return s == 0
    # if at leaf node
    if (not t.left) and (not t.right):
        return t.value == s

    # if not leaf node yet, then we have at least 1 sub-tree, and we check a sub-tree depending on if it exists or not, so can use an indicator here (todo)
    check_left = (t.left != None) * hasPathWithGivenSum(t.left, s - t.value)
    check_right = (t.right != None) * hasPathWithGivenSum(t.right, s - t.value)
    return bool(check_left) or bool(check_right)
