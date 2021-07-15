class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        # write your code here
        if not A:
            return

        A.sort()
        left, right = 0, 1
        while right < len(A):
            if A[left] != A[right]:
                return A[left]
            left += 2
            right += 2

        return A[left]

if __name__ == '__main__':
    s = Solution()
    A = [1,2,2]
    print(s.singleNumber(A))