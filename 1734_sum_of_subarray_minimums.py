class Solution:
    """
    @param A: an array
    @return: the sum of subarray minimums
    """
    def sumSubarrayMins(self, A):
        # Write your code here.
        if not A:
            return 0

        res = 0
        stk = []
        A = [0] + A + [0]
        for i, val in enumerate(A):
            while stk and val < A[stk[-1]]:
                j = stk.pop()
                k = stk[-1]
                res += A[j] * (i - j) * (j - k)
            stk.append(i)

        return res % (10**9 + 7)