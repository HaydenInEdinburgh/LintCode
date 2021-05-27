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
    @param nums: the sorted array
    @return: the root of the tree
    """
    def convertSortedArraytoBinarySearchTree(self, nums):
        # Write your code here.
        if not nums:
            return
        root = self.helper(nums, 0, len(nums)-1)
        return root

    def helper(self, numbers, start, end):
        if (start > end):
            return
        node = TreeNode(numbers[(start +end)//2])
        node.left = self.helper(numbers, start, (start +end)//2 -1)
        node.right = self.helper(numbers, (start + end) // 2 + 1, end)

        return node



