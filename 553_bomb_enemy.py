import collections

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


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
        res = 0
        for i in range(m):
            for j in range(n):
                node = grid[i][j]
                if node != '0':
                    continue
                kills = self.explode(i, j, grid)
                res = max(res, kills)
        return res

    def explode(self, b_x, b_y, grid):
        queue = collections.deque([(b_x, b_y, (0, 0))])
        kills = 0
        while queue:
            x, y, direction = queue.popleft()
            if direction == (0, 0):
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if not self.valid(nx, ny, grid):
                        continue
                    if grid[nx][ny] == 'W':
                        continue
                    if grid[nx][ny] == 'E':
                        kills += 1
                    queue.append((nx, ny, (dx, dy)))
            else:
                dx, dy = direction[0], direction[1]
                nx, ny = x + dx, y + dy
                if not self.valid(nx, ny, grid):
                    continue
                if grid[nx][ny] == 'W':
                    continue
                if grid[nx][ny] == 'E':
                    kills += 1
                queue.append((nx, ny, (dx, dy)))

        return kills

    def valid(self, x, y, grid):
        m, n = len(grid), len(grid[0])
        return 0 <= x < m and 0 <= y < n

if __name__ == '__main__':
    s = Solution()
    grid =["0E00","E0WE","0E00"]
    print(s.maxKilledEnemies(grid))
