class Solution:
    """
    @param matrix: A lsit of lists of integers
    @return: nothing
    """
    def setZeroes(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return []

        zero_col = set()
        zero_row = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not matrix[i][j]:
                    zero_row.add(i)
                    zero_col.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zero_row or j in zero_col:
                    matrix[i][j] = 0


if __name__ == '__main__':
    s = Solution()
    matrix = [[1,2,3],[4,0,6],[7,8,9]]
    s.setZeroes(matrix)
    print(matrix)