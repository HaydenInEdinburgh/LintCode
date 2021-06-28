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
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameterOfBinaryTree(self, root):
        # write your code here
        if not root:
            return 0

        _, diameter = self.helper(root)
        return diameter

    def helper(self, node):
        if not node:
            return 0, 0

        left_longest, left_dia = self.helper(node.left)
        right_longest, right_dia = self.helper(node.right)

        longest = max(left_longest, right_longest) +1
        diameter = max(left_dia, right_dia, left_longest + right_longest)

        return longest, diameter