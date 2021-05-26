"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from idlelib.tree import TreeNode


class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        if not root:
            return None

        stack = []
        self.toMin(root, stack)

        for i in range(k-1):
            node = stack.pop().right
            if node:
                self.toMin(node, stack)

        return stack[-1].val

    def toMin(self, root, stack):
        while root:
            stack.append(root)
            root = root.left

class Solutino2:
    def kthSmallest(self, root, k):
        if not root:
            return

        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]

        for i in range(k):
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

            if not stack:
                return None

        return stack[-1].val

