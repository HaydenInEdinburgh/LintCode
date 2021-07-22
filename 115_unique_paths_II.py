class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if not m or not n: return 0

        dp = [[0]*n for _ in range(m)]
        #init
        dp[0][0] = 1
        for i in range(m):
            if obstacleGrid[i][0]:
                break
            dp[i][0] = 1

        for i in range(n):
            if obstacleGrid[0][i]:
                break
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

if __name__ == '__main__':
    s = Solution()
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    print(s.uniquePathsWithObstacles(obstacleGrid))