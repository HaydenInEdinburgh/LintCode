# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.res = 0
        maximum = - sys.maxsize
        self.dfs(root, maximum)

        return self.res

    def dfs(self, curNode, maximum):
        if not curNode:
            return

        if curNode.val >= maximum:
            # print(curNode.val)
            self.res += 1

        self.dfs(curNode.left, max(curNode.val, maximum))
        self.dfs(curNode.right, max(curNode.val, maximum))
