# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.maxPath = 0

        self.get_deepest(root)

        return self.maxPath

    def get_deepest(self, node):

        left_deepest = self.get_deepest(node.left)[1] + 1 if node.left else 0
        right_deepest = self.get_deepest(node.right)[0] + 1 if node.right else 0

        self.maxPath = max(self.maxPath, left_deepest, right_deepest)

        return left_deepest, right_deepest
