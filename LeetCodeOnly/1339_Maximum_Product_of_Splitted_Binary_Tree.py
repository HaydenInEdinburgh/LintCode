# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root) -> int:
        if not root:
            return 0

        self.node_sum_dict = []
        root_sum = self.get_sum(root)
        res = - float('inf')
        for n in self.node_sum_dict:
            res = max(res, (root_sum -n)*n)

        return res % (10**9 + 7)

    def get_sum(self, root):
        if not root:
            return 0
        left = self.get_sum(root.left)
        right = self.get_sum(root.right)

        self.node_sum_dict.append(root.val + left + right)

        return root.val + left + right
