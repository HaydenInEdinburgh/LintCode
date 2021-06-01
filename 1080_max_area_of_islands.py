import sys


class Solution:
    """
    @param grid: a 2D array
    @return: the maximum area of an island in the given 2D array
    """

    def maxAreaOfIsland(self, grid):
        # Write your code here
        if not grid or not grid[0]:
            return 0

        maximum = 0
        m, n = len(grid), len(grid[0])
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    tmp = self.dfs(x, y, grid, 1)
                    print(tmp)
                    maximum = max(tmp, maximum)

        return maximum

    def dfs(self, x, y, grid, area):
        grid[x][y] = 0
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if not self.isValid(grid, nx, ny):
                continue
            if not grid[nx][ny]:
                continue
            area = 1 + self.dfs(nx, ny, grid, area)

        return area

    def isValid(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

if __name__ == '__main__':
    s = Solution()
    input = [[1]]
    print(s.maxAreaOfIsland(input))