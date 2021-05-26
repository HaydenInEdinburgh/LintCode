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
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        if not root:
            return
        lower_stack, upper_stack = [], []
        res = []
        # upper_stack => upper bound of the target [desc]
        # lower_stack => lower bound of the target [asc]

        cur = root
        while cur:
            upper_stack.append(cur)
            cur = cur.left

        cur = root
        while cur:
            lower_stack.append(cur)
            cur = cur.right

        while len(upper_stack) >0 and upper_stack[-1].val < target:
            self.move_upper(upper_stack)
        while len(lower_stack) >0 and lower_stack[-1].val >= target:
            self.move_lower(lower_stack)

        for i in range(k):
            if not lower_stack:
                res.append(upper_stack[-1].val)
                self.move_upper(upper_stack)
            elif not upper_stack:
                res.append(lower_stack[-1].val)
                self.move_lower(lower_stack)
            else:
                upper, lower = upper_stack[-1].val, lower_stack[-1].val
                if abs(upper - target) < abs(lower - target):
                    res.append(upper)
                    self.move_upper(upper_stack)
                else:
                    res.append(lower)
                    self.move_lower(lower_stack)

        return res

    def move_upper(self, stack):
        cur = stack.pop()
        if cur.right:
            cur = cur.right
            while cur:
                stack.append(cur)
                cur = cur.left

    def move_lower(self, stack):
        cur = stack.pop()
        if cur.left:
            cur = cur.left
            while cur:
                stack.append(cur)
                cur = cur.right