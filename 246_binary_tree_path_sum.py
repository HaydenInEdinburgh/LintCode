"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum2(self, root, target):
        # write your code here
        if not root:
            return []

        res = []
        self.find_path(root, target, res)
        return res

    def find_path(self, curNode, target, res):
        if not curNode:
            return

        self.dfs(curNode, [], target, res)

        self.find_path(curNode.left, target, res)
        self.find_path(curNode.right, target, res)

    def dfs(self, root, path, target, res):
        if not root:
            return

        path.append(root.val)
        if root.val == target:
            res.append(path[:])

        self.dfs(root.left, path, target-root.val, res)
        self.dfs(root.right, path, target-root.val, res)

        path.pop()