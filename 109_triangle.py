class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        if not triangle:
            return 0
        n = len(triangle)
        dp = [[0]*n for _ in range(n)]

        #init
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            dp[i % 2][0] = dp[(i-1) % 2][0] + triangle[i][0]
            dp[i % 2][i] = dp[(i-1) % 2][i-1] + triangle[i][i]
            for j in range(1, i):
                dp[i % 2][j] = min(dp[(i-1) % 2][j-1], dp[(i-1) % 2][j]) + triangle[i][j]

        return min(dp[(n-1)  % 2])

if __name__ == '__main__':
    s = Solution()
    triangle = [
        [2],
        [3, 2],
        [6, 5, 7],
        [4, 4, 8, 1]
    ]
    print(s.minimumTotal(triangle))