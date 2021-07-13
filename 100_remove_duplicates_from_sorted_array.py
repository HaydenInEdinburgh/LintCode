class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        if len(nums) <= 1:
            return len(nums)

        start = left = 0
        n = len(nums)

        while left < n:
            while left < n and nums[start] == nums[left]:
                left += 1
            if left < n:
                nums[start + 1] = nums[left]
                start += 1
                left += 1

        nums = nums[:start+ 1]
        return start +1
if __name__ == '__main__':
    s = Solution()
    nums = [-10,0,1,2,3]
    print(s.removeDuplicates(nums))