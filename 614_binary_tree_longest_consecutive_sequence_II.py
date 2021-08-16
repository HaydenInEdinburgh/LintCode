"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive2(self, root):
        # write your code here
        if not root:
            return 0
        length, _, _ = self.helper(root)

        return length

    def helper(self, root):
        if not root:
            return 0, 0, 0
        leftLen, leftDown, leftUp = self.helper(root.left)
        rightLen, rightDown, rightUp = self.helper(root.right)

        length, down, up = 0, 0, 0
        if root.left and root.val +1 == root.left.val:
            down = max(down, leftDown +1)

        if root.left and root.val -1 == root.left.val:
            up = max(up, leftUp +1)

        if root.right and root.val +1 == root.right.val:
            down = max(down, rightDown +1)

        if root.right and root.val -1 == root.right.val:
            up = max(up, rightUp +1)

        length = max(up + 1 + down, leftLen, rightLen)

        return length, down, up
