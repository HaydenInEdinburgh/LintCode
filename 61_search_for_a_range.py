class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if not A:
            return [-1, -1]

        start = self.get_start(A, target)
        end = self.get_end(A, target)

        return [start, end]

    def get_start(self, A, target):
        l, r = 0, len(A)-1
        while l+1 <r:
            mid = (l+r)//2
            if A[mid] < target:
                l = mid
            else:
                r = mid

        if A[l] == target:
            return l
        if A[r] == target:
            return r
        return -1

    def get_end(self, A, target):
        l, r = 0, len(A) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if A[mid] <= target:
                l = mid
            else:
                r = mid

        if A[r] == target:
            return r
        if A[l] == target:
            return l
        return -1