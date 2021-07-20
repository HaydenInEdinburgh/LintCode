class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        dp = [[False] * (m+1) for _ in range(n+1)]

        dp[0][0] = True
        for i in range(1, n+1):
            dp[i][0] = True
            for j in range(1, m+1):
                dp[i][j] = dp[i-1][j] or dp[i-1][j-A[i-1]] if j >= A[i-1] else dp[i-1][j]
        print(dp)
        for i in range(m, -1, -1):
            if dp[n][i]:
                return i

        return 0

if __name__ == '__main__':
    s = Solution()
    m = 10
    A = [3, 4, 8, 5]
    print(s.backPack(m, A))