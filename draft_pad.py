class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        if not m:
            return 0
        if not A or not V:
            return 0
        n = len(A)
        backpack = [[0] * (m+1) for _ in range(n+1)]
        for i in range(1, m+1):
            backpack[0][i] = 0

        for i in range(1, n+1):
            backpack[i][0] = 0
            for j in range(1, m+1):
                backpack[i][j] = backpack[i-1][j]
                w_ith, v_ith = A[i-1], V[i-1]
                if j >= w_ith and backpack[i-1][j-w_ith] != -1:
                    backpack[i][j] = max(backpack[i-1][j], backpack[i-1][j-w_ith] + v_ith)

        return max(backpack[-1])



if __name__ == '__main__':
