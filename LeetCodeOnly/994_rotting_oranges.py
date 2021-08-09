import collections

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    def orangesRotting(self, grid) -> int:
        m, n= len(grid), len(grid[0])
        if not m or not n:
            return 0

        rottens, fresh_num = self.get_rottens(grid)
        queue = collections.deque(rottens)
        visited = set(rottens)
        res = 0
        while queue:
            if not fresh_num:
                return res
            res += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in DIRECTIONS:
                    nx, ny = x+dx, y+dy
                    if not self.valid(grid, nx, ny) or (nx, ny) in visited:
                        continue
                    if grid[nx][ny] == 0:
                        continue
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    fresh_num -= 1
                    if fresh_num == 0:
                        return res

        if fresh_num > 0:
            return -1
        return res

    def get_rottens(self, grid):
        m, n = len(grid), len(grid[0])
        rottens = []
        fresh_num = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_num += 1
                if grid[i][j] == 2:
                    rottens.append((i, j))

        return rottens, fresh_num

    def valid(self, grid, x, y):
        return 0<= x< len(grid) and 0<= y< len(grid[0])

if __name__ == '__main__':
    s = Solution()
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(s.orangesRotting(grid))