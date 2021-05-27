import collections


class Solution:
    """
    @param tickets:
    @return: nothing
    """

    def findItinerary(self, tickets):
        graph = self.build_graph(tickets)

        results = []
        self.dfs(graph, "JFK", ["JFK"], results, len(tickets))
        print(results)
        return results[0]

    def build_graph(self, tickets):
        graph = {}
        for depart, arrival in tickets:
            if depart not in graph:
                graph[depart] = [arrival]
            else:
                graph[depart].append(arrival)
            if arrival not in graph:
                graph[arrival] = []

        for depart, arrivals in graph.items():
            graph[depart] = sorted(arrivals)
        return graph

    def dfs(self, graph, curr, path, results, total):
        if results:
            return
        if len(path) == total +1:
            print(path)
            results.append(path[:])
            return

        for next in graph[curr][:]:
            path.append(next)
            graph[curr].remove(next)
            self.dfs(graph, next, path, results, total)
            path.pop()
            graph[curr].append(next)

if __name__ == '__main__':
    input = [["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"], ["JFK","SFO"]]
    s = Solution()
    output = s.findItinerary(input)