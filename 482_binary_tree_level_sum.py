"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import collections


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of the binary tree
    @param level: the depth of the target level
    @return: An integer
    """
    def levelSum(self, root, level):
        # write your code here
        if not root or not level: return 0

        queue = collections.deque([root])
        cur_level = 0
        res = 0
        while queue:
            cur_level += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if level == cur_level:
                    res += node.val
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

        return res