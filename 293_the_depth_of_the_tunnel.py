import collections

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    """
    @param matrix: the matrix in problem
    @return: the depth of the tunnel.
    """
    def FindDepth(self, matrix):
        m, n = len(matrix), len(matrix[0])
        if not m or not n: return 0

        start, end = (0, 0), (0, n-1)
        queue = collections.deque([start])
        visited = {start}
        deepest = 0

        while queue:
             x, y = queue.popleft()
             for dx, dy in DIRECTIONS:
                 nx, ny = x+dx, y+dy
                 if not self.valid(matrix, nx, ny) or (nx, ny) in visited:
                     continue
                 if matrix[nx][ny] != 1:
                     continue
                 if (nx, ny) == end:
                     break
                 deepest = max(deepest, nx)
                 queue.append((nx, ny))
                 visited.add((nx, ny))

        return deepest

    def valid(self, matrix, x, y):
        return 0<= x< len(matrix) and 0<= y< len(matrix[0])

if __name__ == '__main__':
    s = Solution()
    matrix = [[1,0,0,0,1],[1,1,0,0,1],[0,1,0,1,1],[0,1,1,1,0],[0,0,0,0,0]]
    print(s.FindDepth(matrix))