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
    @param root: the root
    @return: all the values with the highest frequency in any order
    """

    def findFrequentTreeSum(self, root):
        # Write your code here
        if not root:
            return []

        sum_cnt = {}
        self.get_sum(root, sum_cnt)
        max_cnt = max(sum_cnt.values())
        return [x for x, v in sum_cnt.items() if v == max_cnt]


    def get_sum(self, root, sum_cnt):
        if not root:
            return 0

        left_sum = self.get_sum(root.left, sum_cnt)
        right_sum = self.get_sum(root.right, sum_cnt)
        cur_sum = left_sum + right_sum + root.val
        sum_cnt[cur_sum] = sum_cnt.get(cur_sum, 0) + 1

        return cur_sum