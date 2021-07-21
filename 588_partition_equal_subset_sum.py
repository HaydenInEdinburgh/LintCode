class Solution:
    """
    @param nums: a non-empty array only positive integers
    @return: true if can partition or false
    """
    def canPartition(self, nums):
        # write your code here
        s = sum(nums)
        if s % 2 == 1:
            return False
        target = s // 2
        dp = [False] * (target +1)
        dp[0] = True
        for x in nums:
            for i in range(target, x-1, -1):
                dp[i] = dp[i] or dp[i-x]
        return dp[target]



if __name__ == '__main__':
    s = Solution()
    nums = [1,4,5,6,1,2,4,1,3,4,1,2,4,5,1,91,4,5,6,1,2,4,1,3,4,1,2,4,5,1]
    print(s.canPartition(nums))