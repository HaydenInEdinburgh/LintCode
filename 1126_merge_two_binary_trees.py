"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param t1: the root of the first tree
    @param t2: the root of the second tree
    @return: the new binary tree after merge
    """
    def mergeTrees(self, t1, t2):
        # Write your code here
        if not t1 and not t2:
            return

        if not t1:
            return t2
        if not t2:
            return t1
        new_head = TreeNode(t1.val + t2.val)
        new_head.left = self.mergeTrees(t1.left, t2.left)
        new_head.right = self.mergeTrees(t1.right, t2.right)

        return new_head