import collections

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    """
    @param targetMap:
    @return: nothing
    """
    def shortestPath(self, targetMap):
        # Write your code here
        m, n = len(targetMap), len(targetMap[0])
        if not m or not n:
            return

        visited = {(0, 0)}
        queue = collections.deque([(0, 0)])
        dis = 0

        while queue:
            dis += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in DIRECTIONS:
                    nx, ny = x+dx, y+dy
                    if not self.isValid(nx, ny, targetMap, visited):
                        continue
                    if targetMap[nx][ny] == 0:
                        print((nx, ny), dis)
                        queue.append((nx, ny))
                        visited.add((nx, ny))
                    elif targetMap[nx][ny] == 2:
                        return dis

        return -1

    def isValid(self, x, y, targetMap, visited):
        if (x, y) in visited:
            return False
        if not 0<= x< len(targetMap) or not 0<= y< len(targetMap[0]):
            return False
        if targetMap[x][y] == 1:
            return False
        return True

if __name__ == '__main__':
    s = Solution()
    targetMap = [[0,0,1,0],[0,1,2,0],[1,1,0,1]]
    print(s.shortestPath(targetMap))