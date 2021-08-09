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
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        # write your code here
        if not root:
            return 0

        self.maximum = -sys.maxsize
        self.helper(root)
        return self.maximum

    def helper(self, root):
        if not root:
            return 0
        left_max = self.helper(root.left)
        right_max = self.helper(root.right)

        self.maximum = max(self.maximum, root.val,\
                           right_max+root.val+left_max, \
                           root.val+left_max, root.val+right_max)

        return max(root.val, root.val+left_max, root.val+right_max)