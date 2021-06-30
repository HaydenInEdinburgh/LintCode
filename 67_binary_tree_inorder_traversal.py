"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        if not root:
            return []

        res = []
        self.inorder(root, res)
        return res

    def inorder(self, root, nums):
        if not root:
            return None

        self.inorder(root.left, nums)
        nums.append(root.val)
        self.inorder(root.right, nums)
