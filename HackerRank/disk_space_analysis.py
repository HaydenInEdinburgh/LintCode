import sys
from collections import deque
class Solution:
    def segment(self, x, space):
        if not space:
            return []
        queue = deque([])
        res = - sys.maxsize
        for i in range(x):
            while queue and space[i] <= space[queue[-1]]:
                queue.pop()
            queue.append(i)

        n = len(space)
        for i in range(x, n):
            res = max(res, space[queue[0]])
            while queue and queue[0] <= i-x:
                queue.popleft()

            while queue and space[i] <= space[queue[-1]]:
                queue.pop()

            queue.append(i)
        res = max(res, space[queue[0]])
        return res

if __name__ == '__main__':
    s = Solution()
    space = [2, 5, 4, 6, 8]
    x = 3
    print(s.segment(x, space))