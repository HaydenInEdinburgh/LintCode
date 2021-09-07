DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    """
    @param grids: a integer two-dimensional array
    @return: return the maximum sum of golds
    """
    def FindMaximumGold(self, grids):
        # write your code here
        if not grids:
            return 0

        m, n = len(grids), len(grids[0])
        self.MAXIMUM = 0
        for i in range(m):
            for j in range(n):
                if grids[i][j] == 0:
                    continue
                visited = {(i, j)}
                self.explore(i, j, grids, grids[i][j], visited)

        return self.MAXIMUM

    def explore(self, x, y, grids, cur, visited):
        if grids[x][y] == 0:
            self.MAXIMUM = max(self.MAXIMUM, cur)
            return

        for dx, dy in DIRECTIONS:
            nx, ny = x+dx, y+dy
            if not self.valid(nx, ny, grids):
                continue
            if (nx, ny) in visited:
                continue
            visited.add((nx, ny))
            self.explore(nx, ny, grids, grids[nx][ny] + cur, visited)
            visited.remove((nx, ny))

    def valid(self, x, y, grids):
        m, n = len(grids), len(grids[0])
        return 0 <= x <m and 0 <= y <n

if __name__ == '__main__':
    s = Solution()
    grids = [[1,2,0,0],[0,0,2,2]]
    print(s.FindMaximumGold(grids))