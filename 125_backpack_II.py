import sys


class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        if not A:
            return 0

        n = len(A)
        dp = [[0] * (m+1) for _ in range(n+1)]
        #init
        dp[0][0] = 0 # 0 item, 0 weight and 0 value
        for w in range(1, m+1):
            dp[0][w] = -1 # 0 item can't get a positive weight

        for i in range(1, n+1):
            dp[i][0] = 0
            for j in range(1, m+1):
                dp[i][j] = dp[i-1][j]
                if j >= A[i-1] and dp[i-1][j - A[i-1]] != -1:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i-1]] + V[i-1])

        return max(dp[n])

if __name__ == '__main__':
    s = Solution()
    m = 10
    A = [2, 3, 5, 7]
    V = [1, 5, 2, 4]
    print(s.backPackII(m, A, V))