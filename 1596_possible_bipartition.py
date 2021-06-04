class Solution:
    """
    @param N:  sum of the set
    @param dislikes: dislikes peoples
    @return:  if it is possible to split everyone into two groups in this way
    """
    def possibleBipartition(self, N, dislikes):
        # Write your code here.
        if not N or not dislikes:
            return True

        dis_graph = self.get_dislikes(N, dislikes)
        visited = [0 for _ in range(N)]

        for i in range(1, N+1):
            if visited[i-1] == 0:
                visited[i-1] = 1
                if not self.dfs(i, visited, dis_graph):
                    return False

        return True

    def dfs(self, cur, visited, dis_graph):
        for j in dis_graph[cur]:
            if not visited[j-1]:
                visited[j-1] = - visited[cur-1]
                if not self.dfs(j, visited, dis_graph):
                    return False
            elif visited[j-1] == visited[cur-1]:
                return False
        return True





    def get_dislikes(self, N, dislikes):
        dis_graph = {i: set() for i in range(1, N+1)}
        for a, b in dislikes:
            dis_graph[a].add(b)
            dis_graph[b].add(a)

        return dis_graph