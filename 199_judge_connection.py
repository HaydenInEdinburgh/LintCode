import collections
class Solution:
    """
    @param arr: the arr
    @param k: the k
    @return: if all instances of value k in arr are connected
    """
    def judgeConnection(self, arr, k):
        # Write your code here.
        m, n = len(arr), len(arr[0])
        if not m or not n:
            return

        start_node = None
        total = 0
        for i in range(m):
            for j in range(n):
                if arr[i][j] == k:
                    total += 1
                    if not start_node:
                        start_node = (i, j)
        print(total)
        queue = collections.deque([start_node])
        visited = {start_node}
        while queue:
            x, y = queue.popleft()
            print(x, y)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x+dx, y+dy
                if not self.valid(arr, nx, ny) or (nx, ny) in visited:
                    continue
                if arr[nx][ny] == k:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
        print(visited)
        return len(visited) == total

    def valid(self, arr, x, y):
        return 0<= x<len(arr) and 0<= y<len(arr[0])

if __name__ == '__main__':
    s = Solution()
    arr = [[2 ,2 ,2 ,0],[0, 0, 0, 2],[0,1,0,2],[1,1,1,2]]
    k = 1
    print(s.judgeConnection(arr, k))