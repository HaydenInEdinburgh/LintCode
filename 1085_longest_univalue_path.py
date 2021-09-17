"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root:
    @return: the length of the longest path where each node in the path has the same value
    """
    def longestUnivaluePath(self, root):
        # Write your code here
        if not root:
            return 0
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return 0, -1

        l_path, l_rootval = self.dfs(node.left)
        r_path, r_rootval = self.dfs(node.right)

        if l_rootval == node.val and r_rootval == node.val:
            self.res = max(self.res, l_path + r_path)
            return max(l_path, r_path) +1, node.val
        elif l_rootval == node.val:
            self.res = max(self.res, l_path)
            return l_path+1, node.val
        elif r_rootval == node.val:
            self.res = max(self.res, r_path)
            return r_path+1, node.val
        else:
            return 1, node.val