class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        if not m or not n:
            return 0

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(1, m):
            dp[i][0] = 1

        for j in range(1, n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]


if __name__ == '__main__':
    s = Solution()
    m = 3
    n = 3
    print(s.uniquePaths(m, n))