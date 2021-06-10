"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
import collections

DIRECTIONS = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        m, n = len(grid), len(grid[0])
        if not m or not n:
            return -1
        if (source.x, source.y) == (destination.x, destination.y):# source is also destination
            return 0
        queue = collections.deque([source])
        visited = {(source.x, source.y): 0}
        dis = 0
        while queue:
            dis += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for dx, dy in DIRECTIONS:
                    nx, ny = node.x + dx, node.y + dy
                    if not self.isValid(grid, nx, ny, visited):
                        continue
                    if (nx, ny) == (destination.x, destination.y):
                        return dis
                    visited[(nx, ny)] = dis
                    queue.append(Point(nx, ny))

        return -1

    def isValid(self, grid, x, y, visited):
        if x<0 or x>= len(grid) or y<0 or y>= len(grid[0]):
            return False
        if grid[x][y] == 1:
            return False
        if (x, y) in visited:
            return False
        return True

if __name__ == '__main__':
    s = Solution()
    input = [[0,0,0],[0,0,0],[0,0,0]]
    source = Point(1, 1)
    destination = Point(1, 1)
    print(s.shortestPath(input, source, destination))