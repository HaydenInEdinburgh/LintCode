class Solution:
    """
    @param strs: an array with strings include only 0 and 1
    @param m: An integer
    @param n: An integer
    @return: find the maximum number of strings
    """
    def findMaxForm(self, strs, m, n):
        # write your code here
        dp = [[0] * (n+1) for _ in range(m+1)]

        for s in strs:
            cost = self.count(s)
            for i in range(m, cost[0]-1, -1):
                for j in range(n, cost[1]-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i- cost[0]][j - cost[1]] + 1)

        return dp[-1][-1]
    def count(self, s):
        cost = [0] * 2
        for i in range(len(s)):
            cost[int(s[i])] += 1
        return cost