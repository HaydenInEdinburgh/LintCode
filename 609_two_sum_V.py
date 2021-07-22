class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        if len(nums) <= 1: return 0
        nums.sort()
        res = 0
        l, r = 0, len(nums)-1

        while l < r:
            cur_sum = nums[l] + nums[r]
            if cur_sum <= target:
                res += (r - l)
                l += 1
                r = len(nums)-1
            else:
                r -= 1

        return res

if __name__ == '__main__':
    s = Solution()
    nums = [1]
    target = 1
    print(s.twoSum5(nums, target))