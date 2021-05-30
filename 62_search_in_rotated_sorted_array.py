class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if not A or not target:
            return -1

        start, end = 0, len(A) -1

        while start+1 < end:
            mid = (start +end)//2
            if A[mid] >= A[start]: #topleft
                if A[start] <= target < A[mid]:
                    end = mid
                else:
                    start = mid
            else:#bottomright
                if A[mid] <= target < A[end]:
                    start = mid
                else:
                    end = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end

        return -1
