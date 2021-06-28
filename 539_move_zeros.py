class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        if len(nums) <= 1: return nums

        n = len(nums)

        left, right = 0, 0
        while right < n:
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
            right += 1

        while left < n:
            nums[left] = 0
            left += 1

        return nums