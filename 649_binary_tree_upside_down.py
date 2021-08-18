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

class Solution:
    """
    @param root: the root of binary tree
    @return: new root
    """
    def upsideDownBinaryTree(self, root):
        # write your code here
        if not root:
            return None
        return self.dfs(root)

    def dfs(self, node):
        if not node.left:
            return node

        newroot = self.dfs(node.left)
        node.left.right = node
        node.left.left = node.right
        node.left = None
        node.right = None
        return newroot
