class Solution:
    def findCircleNum(self, isConnected) -> int:
        if not isConnected or not isConnected[0]:
            return 0

        res = 0
        visited = set()
        n = len(isConnected)
        for i in range(n):
            if i in visited:
                continue
            res += 1
            self.dfs(isConnected, i, visited)

        return res

    def dfs(self, isConnected, x, visited):
        for i in range(len(isConnected)):
            if i in visited or not isConnected[x][i] or x == i:
                continue
            visited.add(i)
            self.dfs(isConnected, i, visited)

if __name__ == '__main__':
    s = Solution()
    isConnectead = [[1,1,0],[1,1,0],[0,0,1]]
    print(s.findCircleNum(isConnectead))