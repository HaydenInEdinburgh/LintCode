class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return  0

        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(2)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                elif i == 0:
                    dp[i%2][j] = dp[i%2][j-1] + grid[i][j]
                elif j == 0:
                    dp[i%2][j] = dp[(i-1)%2][j] + grid[i][j]
                else:
                    dp[i%2][j] = min(dp[(i-1)%2][j], dp[i%2][j-1]) + grid[i][j]

        return dp[(m-1)%2][-1]

if __name__ == '__main__':
    s = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(s.minPathSum(grid))