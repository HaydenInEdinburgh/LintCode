class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices:
            return 0

        k = 2
        n = len(prices)
        dp = [[0]*n for _ in range(k+1)]
        for i in range(1, k+1):
            max_diff = float('-inf')
            for j in range(1, n):
                max_diff = max(max_diff, dp[i-1][j-1] - prices[j-1])
                dp[i][j] = max(dp[i][j-1], prices[j] + max_diff)

        return dp[k][n-1]
    