import collections
class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """

    def maxKilledEnemies(self, grid):
        # write your code here
        m, n = len(grid), len(grid[0])
        if not m or not n:
            return 0
        up = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]
        left = [[0] * n for _ in range(m)]
        right = [[0] * n for _ in range(m)]

        #up
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'W':
                    continue
                if grid[i][j] == 'E':
                    up[i][j] = 1
                if i > 0:
                    up[i][j] += up[i-1][j]

        #down
        for i in range(m-1, -1, -1):
            for j in range(n):
                if grid[i][j] == 'W':
                    continue
                if grid[i][j] == 'E':
                    down[i][j] = 1
                if i < m-1:
                    down[i][j] += down[i+1][j]

        #left
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'W':
                    continue
                if grid[i][j] == 'E':
                    left[i][j] = 1
                if j >0:
                    left[i][j] += left[i][j-1]

        #right
        for i in range(m):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 'W':
                    continue
                if grid[i][j] == 'E':
                    right[i][j] = 1
                if j <n-1:
                    right[i][j] += right[i][j+1]

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    res = max(res, up[i][j] + down[i][j]+ left[i][j]+ right[i][j])

        return res


if __name__ == '__main__':
    s = Solution()
    grid =["0E00","E0WE","0E00"]
    print(s.maxKilledEnemies(grid))
