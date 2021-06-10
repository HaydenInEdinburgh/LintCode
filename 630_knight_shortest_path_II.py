import sys
from collections import deque
DIRECTIONS = [
    (-1, -2),
    (1, -2),
    (-2, -1),
    (2, -1),
]
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

        dp = [[sys.maxsize] * 3 for _ in range(n)]

        #init
        dp[0][0] = 0

        #FUNCTION
        for j in range(m):
            for i in range(n):
                if grid[i][j]:
                    continue # barrier
                for dx, dy in DIRECTIONS:
                    nx, ny = i+dx, j+dy #nx ,ny are actually pre step
                    if 0<= nx< n and 0<= ny< m:
                        dp[i][j %3] = min(dp[i][j%3], dp[nx][ny%3] +1)
        print(dp)
        if dp[n-1][(m-1)%3] == sys.maxsize:
            return -1
        return dp[n-1][(m-1)%3]

if __name__ == '__main__':
    s = Solution_DP()
    input = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    print(s.shortestPath2(input))