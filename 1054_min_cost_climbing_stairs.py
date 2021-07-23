class Solution:
    """
    @param cost: an array
    @return: minimum cost to reach the top of the floor
    """
    def minCostClimbingStairs(self, cost):
        # Write your code here
        if not cost:
            return 0

        n = len(cost)
        dp = [0] * n
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        return min(dp[-2:])

if __name__ == '__main__':
    s = Solution()
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(s.minCostClimbingStairs(cost))