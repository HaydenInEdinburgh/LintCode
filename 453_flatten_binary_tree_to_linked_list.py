"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        self.flatten_and_return_last_node(root)

    def flatten_and_return_last_node(self, root):
        if not root:
            return

        left_last = self.flatten_and_return_last_node(root.left)
        right_last = self.flatten_and_return_last_node(root.right)

        if left_last:
            left_last.right = root.right
            root.right = root.left
            root.left = None

        return right_last or left_last or root

class Solution2:
    def flatten(self, root):
        nodelist = []
        self.traverse(root, nodelist)

        for i in range(len(nodelist)-1):
            nodelist[i].right, nodelist[i].left = nodelist[i+1], None

    def traverse(self, root, nodelist):
        if not root:
            return

        nodelist.append(root)
        self.traverse(root.left, nodelist)
        self.traverse(root.right, nodelist)
