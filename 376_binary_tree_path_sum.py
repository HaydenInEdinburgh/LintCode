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
    def binaryTreePathSum(self, root, target):
        # write your code here
        if not root:
            return []

        res = []
        self.dfs(root, [root.val], target-root.val, res)
        return res

    def dfs(self, cur_node, path, target, res):
        if not cur_node.left and not cur_node.right:
            if target == 0:
                res.append(path[:])
            return

        if cur_node.left:
            path.append(cur_node.left.val)
            self.dfs(cur_node.left, path, target-cur_node.left.val, res)
            path.pop()

        if cur_node.right:
            path.append(cur_node.right.val)
            self.dfs(cur_node.right, path, target-cur_node.right.val, res)
            path.pop()
