class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """
    def __init__(self):
        self.m = 0
        self.n = 0
        self.DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def numberofDistinctIslands(self, grid):
        # write your code here
        self.m, self.n = len(grid), len(grid[0])
        if not self.m or not self.n:
            return 0

        islands = set()

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    aIsland = set()
                    self.dfs(i, j, aIsland, grid, i, j)
                    islands.add(tuple(aIsland))

        return len(islands)

    def dfs(self, x, y, aIsland, grid, cur_x, cur_y):
        grid[cur_x][cur_y] = 0
        aIsland.add((x-cur_x, y-cur_y))
        for dx, dy in self.DIRECTIONS:
            nx, ny = cur_x+dx, cur_y+dy
            if nx< 0 or nx >= self.m or ny<0 or ny >= self.n:
                continue
            if grid[nx][ny] == 0:
                continue
            self.dfs(x, y, aIsland, grid, nx, ny)
