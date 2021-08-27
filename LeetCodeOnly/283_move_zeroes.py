class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        l = self.find_first_zero(nums)
        if n <= 1 or l == -1 or l == n-1:
            return

        r = l + 1
        while r < n:
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                # find next zero
                l += 1
                while r< n and l < n and nums[l] != 0:
                    l += 1
                    r += 1
                # find the first non zero after l
                while r < n and nums[r] == 0:
                    r += 1
            else:
                r += 1


    def find_first_zero(self, nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                return i

        return -1