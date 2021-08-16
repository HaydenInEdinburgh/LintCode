"""
Definition for a multi tree node.
class MultiTreeNode(object):
    def __init__(self, x):
        self.val = x
        children = [] # children is a list of MultiTreeNode
"""

import heapq
class Solution:
    # @param {MultiTreeNode} root the root of k-ary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive3(self, root):
        # Write your code here
        if not root:
            return 0

        len, _, _ = self.helper(root)
        return len

    def helper(self, root):
        if not root:
            return 0, 0, 0


        length, down, up = 0, 0, 0
        for child in root.children:
            c_length, c_down, c_up = self.helper(child)
            if child.val == root.val +1:
                down = max(down, c_down+1)
            elif child.val == root.val -1:
                up = max(up, c_up+1)

            length = max(length, c_length)

        length = max(length, down + up +1)

        return length, down, up
