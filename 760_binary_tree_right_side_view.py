"""
Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import collections


class Solution:
    """
    @param root: the root of the given tree
    @return: the values of the nodes you can see ordered from top to bottom
    """
    def rightSideView(self, root):
        # write your code here
        if not root:
            return []

        queue = collections.deque([root])
        view = []

        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if i == n-1:
                    view.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return view