"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def findSubtree(self, root):
        # write your code here
        if not root:
            return None

        self.minimum = sys.maxsize
        self.res = None

        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return 0

        left_w = self.helper(node.left)
        right_w = self.helper(node.right)

        w = node.val + left_w + right_w

        if w < self.minimum:
            self.minimum = w
            self.res = node

        return w