"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        # write your code here
        if not root:
            return 0
        self.max_length = 1
        self.dfs(root, None, 1)

        return self.max_length

    def dfs(self, cur_node, parent_val, length):
        if not cur_node:
            return

        if parent_val and cur_node.val != parent_val+1:
            self.dfs(cur_node, None, 1)
            return

        self.max_length = max(self.max_length, length)

        self.dfs(cur_node.left, cur_node.val, length+1)
        self.dfs(cur_node.right, cur_node.val, length+1)