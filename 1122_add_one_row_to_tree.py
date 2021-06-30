"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

from collections import deque
class Solution:
    """
    @param root: the root of binary tree
    @param v: a integer
    @param d: a integer
    @return: return a TreeNode
    """
    def addOneRow(self, root, v, d):
        # write your code here
        if d == 1:
            new_head = TreeNode(v)
            new_head.left = root
            return new_head

        queue = deque([root])
        cur_d = 1
        while queue and cur_d <= d:
            for _ in range(len(queue)):
                node = queue.popleft()
                if cur_d == d-1:
                    self.add_child(node, v)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            cur_d += 1

        return root

    def add_child(self, node, v):

        left_node = TreeNode(v)
        if node.left:
            left_node.left = node.left
        node.left = left_node

        right_node = TreeNode(v)
        if node.right:
            right_node.right = node.right
        node.right = right_node