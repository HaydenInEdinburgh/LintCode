import sys


class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """
    def maxSquare(self, matrix):
        # write your code here
        m, n = len(matrix), len(matrix[0])
        if not m or not n:
            return 0

        dp = [[0] * n for _ in range(m)]

        #init
        for i in range(n):
            dp[0][i] = matrix[0][i]

        max_width = max(dp[0])
        for i in range(1, m):
            dp[i][0] = matrix[i][0]
            for j in range(1, n):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            max_width = max(max_width, max(dp[i]))
        print(dp)
        return max_width ** 2

if __name__ == '__main__':
    s = Solution()
    matrix = [[0,1]]
    print(s.maxSquare(matrix))

