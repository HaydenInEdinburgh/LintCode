class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # write your code here
        n = len(values)
        if n == 0:
            return False
        if n <= 2:
            return True

        dp = [0] * (n+1)
        for i in range(n-1, -1, -1):
            dp[i] = values[i] - dp[i+1]
            if i + 2 <= n:
                dp[i] = max(dp[i], values[i]+values[i+1] - dp[i+2])

        return dp[0] >= 0