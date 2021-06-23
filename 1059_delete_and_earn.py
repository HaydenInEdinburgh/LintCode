class Solution:
    """
    @param nums: a list of integers
    @return: return a integer
    """
    def deleteAndEarn(self, nums):
        # write your code here
        if not nums:
            return 0

        cnt = [0] * 10001
        for n in nums:
            cnt[n] += 1

        dp = [0] * 10001
        dp[1] = cnt[1]

        for i in range(2, 10001):
            dp[i] = max(dp[i-1], dp[i-2] + i * cnt[i])

        return dp[10000]