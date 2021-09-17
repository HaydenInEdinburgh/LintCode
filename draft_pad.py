class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        # write your code here
        if not m:
            return True
        if not A:
            return False

        backpack = [[False] * (m + 1) for _ in range(len(A) + 1)]
        backpack[0][0] = True  # 0 item can get 0 weight

        for i in range(1, len(A) + 1):
            # ith item
            backpack[i][0] = True
            for j in range(1, m + 1):
                ith = A[i - 1]
                if j > ith:
                    backpack[i][j] = backpack[i - 1][j] or backpack[i - 1][j - ith]
                else:
                    backpack[i][j] = backpack[i - 1][j]
        print(backpack[-1])
        for i in range(m, -1, -1):
            if backpack[len(A)][i]:
                return i

        return 0

if __name__ == '__main__':
    s = Solution()
    m = 10
    A = [3,4,8,5]
    print(s.backPack(m, A))
