"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import collections


class Solution:
    """
    @param root: a root of tree
    @return: return a integer
    """
    def findBottomLeftValue(self, root):
        # write your code here
        if not root:
            return None

        queue = collections.deque([root])
        depth, res = 0, None
        cur = 0
        while queue:
            cur += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if cur > depth:
                    depth = cur
                    res = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res
