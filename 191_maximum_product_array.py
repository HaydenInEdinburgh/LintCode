class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        # write your code here
        if not nums:
            return

        res = prev_max = prev_min = nums[0]

        for n in nums[1:]:
            if n >0:
                cur_max = max(n, prev_max * n)
                cur_min = min(n, prev_min * n)
            else:
                cur_max = max(n, prev_min * n)
                cur_min = min(n, prev_max * n)
            res = max(res, cur_max)
            prev_max, prev_min = cur_max, cur_min

        return res
