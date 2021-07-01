# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not x or not y:
            return False

        queue = deque([root])
        depths, parents = {}, {}
        cur_depth = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                depths[node.val] = cur_depth
                if node.left:
                    queue.append(node.left)
                    parents[node.left.val] = node

                if node.right:
                    queue.append(node.right)
                    parents[node.right.val] = node

            cur_depth += 1
        return depths[x] == depths[ay] and parents[x] != parents[y]