import sys
from collections import deque
DIRECTIONS = [(1,2), (-1,2), (2,1), (-2,1)]
class Solution_BFS:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        des = (m-1, n-1)
        queue = deque([(0, 0)])
        visited = {(0, 0): 0}
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in DIRECTIONS:
                    nx, ny = x+dx, y+dy
                    if not self.isValid(grid, nx, ny, visited):
                        continue
                    queue.append((nx, ny))
                    visited[(nx, ny)] = visited[(x, y)] + 1

        if des in visited:
            return visited[des]
        return -1

    def isValid(self, grid, x, y, visited):
        if x<0 or x>= len(grid) or y<0 or y>= len(grid[0]):
            return False
        if grid[x][y] == 1:
            return False
        if (x, y) in visited:
            return False
        return True

class Solution_DP:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        # write your code here
        n, m = len(grid), len(grid[0])
        if not m or not n:
            return 0

        dp = [[0] * m for _ in range(n)]

        #init
        dp[0][0] = 1
        for j in range(1, m):
            for i in range(n):
                dp[i][j] = sys.maxsize
                if grid[i][j]:
                    continue # barrier
                for dx, dy in DIRECTIONS:
                    nx, ny = i+dx, j+dy
                    if 0<= nx< m and 0<= ny< n:
                        dp[nx][ny] = (dp[nx][], dp[i][j] +1