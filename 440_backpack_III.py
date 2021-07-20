class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """
    def backPackIII(self, A, V, m):
        # write your code here
        if not A or not m:
            return 0

        n = len(A)
        dp = [[0] * (m+1) for _ in range(n+1)]

        dp[0][0] = 0
        for w in range(1, m+1):
            dp[0][w] = -1

        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = dp[i-1][j]
                if j >= A[i-1] and dp[i][j-A[i-1]] != -1:
                    dp[i][j] = max(dp[i][j], dp[i][j - A[i-1]] + V[i-1])

        return max(dp[n])