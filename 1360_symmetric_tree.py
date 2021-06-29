"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

from collections import deque
class Solution:
    """
    @param root: root of the given tree
    @return: whether it is a mirror of itself
    """
    def isSymmetric(self, root):
        # Write your code here
        if not root:
            return True

        queue = deque([root])
        while queue:
            if not self.ifSymmetrical(queue):
                return False
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.val == -1:
                    continue
                queue.append(node.left) if node.left else queue.append(TreeNode(-1))
                queue.append(node.right) if node.right else queue.append(TreeNode(-1))

        return True

    def ifSymmetrical(self, queue):
        left, right = 0, len(queue)-1
        while left < right:
            if queue[left].val != queue[right].val:
                return False
            left += 1
            right -= 1
        return True