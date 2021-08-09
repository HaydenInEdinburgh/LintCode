class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        n = len(A)
        if n <=2: return None

        l, r = 0, len(A)-1

        while l+1< r:
            mid = (l+r)//2
            if self.is_peak(A, mid):
                return mid
            if A[mid-1]< A[mid]:
                l = mid
            else:
                r = mid

        return None

    def is_peak(self, A, mid):
        if mid == 0 or mid == len(A)-1:
            return False
        return A[mid-1] < A[mid] and A[mid] > A[mid+1]


if __name__ == '__main__':
    s = Solution()
    arr = [1, 1, 1]
    print(s.findPeak(arr))