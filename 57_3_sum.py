class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        if not numbers:
            return []

        number_cnt = {}
        for n in numbers:
            number_cnt[n] = number_cnt.get(n, 0) + 1

        nums = sorted(numbers)
        i = 0
        res = []
        while i < len(nums)-2:
            self.twoSum(nums[i+1:], -nums[i], res)
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i-1]:
                i += 1

        return res

    def twoSum(self, nums, target, res):
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] + nums[right] == target:
                res.append([-target, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
