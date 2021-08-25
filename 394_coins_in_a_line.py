class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here
        if not n:
            return False

        if n <= 2:
            return True

        dp = [False] * (n+1)
        dp[1], dp[2] = True, True

        for i in range(3, n+1):
            dp[i] = (dp[i-1] == False) or (dp[i-2] == False)

        return dp[-1]

