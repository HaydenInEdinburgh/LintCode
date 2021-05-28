import collections

DIRECTIONS = [
    (0, 1),
    (0, -1),
    (-1, 0),
    (1, 0),
]
class Solution:
    def ShortestBridge(self, A):
        if not A or not A[0]:
            return 0

        first_land = self.get_first_land(A)
        first_island_lands = self.explore_island(A, first_land[0], first_land[1])

        distance = -1
        queue = collections.deque(first_island_lands)
        visited = set(first_island_lands)

        while queue:
            distance += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in DIRECTIONS:
                    nx, ny = x+dx, y+dy
                    if (nx, ny) in visited:
                        continue
                    if not (0<= nx< len(A) and 0<= ny< len(A[0])):
                        continue
                    if A[nx][ny] == 0:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
                    else:
                        return distance

        return -1

    def get_first_land(self, A):
        for x in range(len(A)):
            for y in range(len(A[0])):
                if A[x][y]:
                    return (x, y)
        return (-1, -1)

    def explore_island(self, A, x, y):

        queue = collections.deque([(x, y)])
        visited = {(x, y)}
        res = []
        while queue:
            x, y = queue.popleft()
            res.append((x, y))
            for dx, dy in DIRECTIONS:
                nx, ny = x+ dx, y+ dy
                if (nx, ny) in visited or not (0<= nx< len(A) and 0<= ny< len(A[0])):
                    continue
                if not A[nx][ny]:
                    continue
                queue.append((nx, ny))
                visited.add((nx, ny))

        return res