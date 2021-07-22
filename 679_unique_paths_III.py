class Solution:
    """
    @param: : an array of arrays
    @return: the sum of all unique weighted paths
    """

    def uniqueWeightedPaths(self, grid):
        # write your codes here

        m, n = len(grid), len(grid[0])
        if not m or not n:
            return 0

        dp = [[set() for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j].add(grid[i][j])
                else:
                    for val in dp[i-1][j]:
                        dp[i][j].add(val + grid[i][j])
                    for val in dp[i][j-1]:
                        dp[i][j].add(val + grid[i][j])

        res = 0
        for n in dp[m-1][n-1]:
            res += n
        return res


if __name__ == '__main__':
    s = Solution()
    grid = [[1,1,2],[1,2,3],[3,2,4]]
    print(s.uniqueWeightedPaths(grid))