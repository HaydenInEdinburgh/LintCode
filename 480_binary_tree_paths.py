"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if not root:
            return []

        res = []
        self.dfs(root, [root.val], res)

        return res

    def dfs(self, root, path, res):
        if not root.left and not root.right:
            path_str = self.draw_path(path[:])
            res.append(path_str)
            return

        if root.left:
            path.append(root.left.val)
            self.dfs(root.left, path, res)
            path.pop()

        if root.right:
            path.append(root.right.val)
            self.dfs(root.right, path, res)
            path.pop()

    def draw_path(self, path):
        return '->'.join([str(n) for n in path])
