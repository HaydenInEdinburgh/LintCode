class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackIV(self, nums, target):
        # write your code here
        if not nums or not target:
            return 0

        n = len(nums)
        dp = [[0] * (target+1) for _ in range(target+1)]
        dp[0][0] = 1

        for i in range(1, n+1):
            dp[i%2][0] = 1
            for j in range(1, target+1):
                dp[i%2][j] = dp[(i-1) %2][j]
                if j - nums[i-1] >= 0:
                    dp[i%2][j] += dp[i%2][j - nums[i-1]]
        return dp[n%2][target]

if __name__ == '__main__':
    s = Solution()
    nums =  [2,3,6,7]
    target = 7
    print(s.backPackIV(nums, target))