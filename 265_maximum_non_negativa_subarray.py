class Solution:
    """
    @param A: an integer array
    @return: return maxium contiguous non-negative subarray sum
    """
    def maxNonNegativeSubArray(self, A):
        # write your code here
        if not A:
            return 0

        tmp, res = 0, -1
        for n in A:
            if n >= 0:
                tmp += n
                res = max(res, tmp)
            else:
                tmp = 0

        return res

if __name__ == '__main__':
    s = Solution()
    A = [1,2,-3,4,5,-6]
    print(s.maxNonNegativeSubArray(A))