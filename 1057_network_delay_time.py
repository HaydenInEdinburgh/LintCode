import heapq
import sys


class Solution:
    """
    @param times: a 2D array
    @param N: an integer
    @param K: an integer
    @return: how long will it take for all nodes to receive the signal
    """

    def networkDelayTime(self, times, N, K):
        # Write your code here
        if not times or not N:
            return 0

        graph = self.get_shortest_path(times, N)
        res = {K: 0}
        visited = set()
        stk = [(0, K)]

        while stk:
            cost, n = heapq.heappop(stk)
            if n in visited:
                continue

            res[n] = cost
            visited.add(n)

            for next, time in graph[n].items():
                if next in visited:
                    continue
                if next in res and res[next] < time+ cost:
                    continue
                res[next] = time+ cost
                heapq.heappush(stk, (time+ cost, next))

        if len(res.keys()) != N:
            return -1
        return max(res.values())

    def dfs(self, shortest_path, cur, res, time, N):
        if cur in res and res[cur] > time:
            res[cur] = time

        res[cur] = min(time, res.get(cur, sys.maxsize))
        for i in range(1, N+1):
            if cur == i or i not in shortest_path[cur]:
                continue
            self.dfs(shortest_path, i, res, time + shortest_path[cur][i], N)

    def get_shortest_path(self, times, N):
        shortest_path = {n: {} for n in range(1, N + 1)}
        for source, target, time in times:
            shortest_path[source][target] = min(shortest_path[source].get(target, sys.maxsize), time)

        return shortest_path

if __name__ == '__main__':
    s = Solution()
    times =  [[1,2,1],[2,1,3]]
    N = 2
    K = 2
    print(s.networkDelayTime(times, N, K))