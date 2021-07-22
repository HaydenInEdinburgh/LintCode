class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        if not nums:
            return []

        l, r = 0, len(nums)-1

        while l < r:
            curSum = nums[l] + nums[r]
            if curSum == target:
                return [l+1, r+1]
            elif curSum < target:
                l += 1
            else:
                r -= 1

        return []

if __name__ == '__main__':
    s = Solution()
    nums = [2, 3]
    target = 5

    print(s.twoSum(nums, target))