class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        m, n = len(matrix), len(matrix[0])
        if not m or not n:
            return 0

        col, row = n-1, 0
        res = 0
        while col >= 0 and row < m:
            cur_num = matrix[row][col]
            if cur_num > target:
                col -= 1
            elif cur_num < target:
                row += 1
            else:
                res += 1
                row += 1

        return res
