class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        if len(nums) < k:
            return []

        l, r = 0, 0
        cur_sum = 0
        res = []
        while r < len(nums):
            cur_sum += nums[r]
            r += 1
            if r-l == k:
                res.append(cur_sum)
                cur_sum -= nums[l]
                l += 1

        return res

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,7,8,5]
    k = 3
    print(s.winSum(nums, k))