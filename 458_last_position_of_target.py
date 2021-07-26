class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def lastPosition(self, nums, target):
        # write your code here
        n = len(nums)
        if not n: return -1

        l, r = 0, n - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid

        if nums[r] == target:
            return r
        if nums[l] == target:
            return l
        return -1