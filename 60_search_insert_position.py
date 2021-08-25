class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if not A: return 0

        l, r = 0, len(A)-1
        #find the first position not less than target
        while l+1 <r:
            mid = (l+r)//2
            if A[mid] < target:
                l = mid
            else:
                r = mid

        if A[l] >= target:
            return l
        if A[r] >= target:
            return r
        return len(A)
