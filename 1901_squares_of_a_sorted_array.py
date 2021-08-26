class Solution_NAIVE:
    """
    @param A: The array A.
    @return: The array of the squares.
    """
    def SquareArray(self, A):
        # write your code here
        if not A:
            return []

        return sorted([n **2 for n in A])

class Solution:
    """
    @param A: The array A.
    @return: The array of the squares.
    """

    def SquareArray(self, A):
        # write your code here
        if not A:
            return []

        l, r = 0, len(A) - 1
        res = []
        while l <= r:
            # print(A[l], A[r])
            if A[l] ** 2 > A[r] ** 2:
                res.append(A[l] ** 2)
                l += 1
            else:
                res.append(A[r] ** 2)
                r -= 1

        return res[::-1]



if __name__ == '__main__':
    s = Solution()
    nums = [-4,-1,0,3,10]
    print(s.SquareArray(nums))