class Solution:
    """
    @param arrays: a list of array
    @param k: An integer
    @return: an integer, K-th largest element in two arrays
    """
    def KthInTwoArrays(self, A, B, k):
        # write your code here
        m, n = len(A), len(B)
        if m +n < k:
            return None

        i, j = m-1, n-1

        while k > 0 and j>=0 and i>=0:
            if A[i] >= B[j]:
                curr = A[i]
                i -= 1
            else:
                curr = B[j]
                j -= 1
            k -= 1

        if k == 0:
            return curr
        if j >= 0:
            return B[j-k+1]
        if i >= 0:
            return A[i-k+1]

if __name__ == '__main__':
    s = Solution()
    A = [1, 3, 5, 6, 9]
    B = [5, 7]
    k = 3
    print(s.KthInTwoArrays(A, B, k))