"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        if not root or not k:
            return []

        nodes = []
        self.inorder(root, nodes)
        return nodes[k-1].val

    def inorder(self, root, nodes):
        if not root:
            return None

        self.inorder(root.left, nodes)
        nodes.append(root)
        self.inorder(root.right, nodes)