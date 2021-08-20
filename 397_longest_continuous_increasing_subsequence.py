class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        if not A:
            return 0
        n = len(A)
        res = 1
        #from left to right
        dp_a = [1] * n
        for i in range(1, n):
            if A[i] > A[i-1]:
                dp_a[i] = dp_a[i-1] +1
                res = max(res, dp_a[i])

        #from right to left
        dp_b = [1] * n
        for j in range(n-2, -1, -1):
            if A[j] > A[j+1]:
                dp_b[j] = dp_b[j+1] +1
                res = max(res, dp_b[j])

        return res

if __name__ == '__main__':
    s = Solution()
    input = [5, 4, 2, 1, 3]
    print(s.longestIncreasingContinuousSubsequence(input))