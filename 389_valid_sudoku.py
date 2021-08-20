class Solution:
    """
    @param board: the board
    @return: whether the Sudoku is valid
    """
    def isValidSudoku(self, board):
        # write your code here
        if not board or not board[0]:
            return
        row = [[False]*9 for _ in range(9)]
        col = [[False]*9 for _ in range(9)]
        rec = [[False]*9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                ele = board[i][j]#row i, col j, rec i//3*3+j//3
                if ele == '.':
                    continue

                ele = int(ele)
                if row[i][ele-1] or col[j][ele-1] or rec[i//3*3+j//3][ele-1]:
                    return False
                row[i][ele-1] = True
                col[j][ele - 1] = True
                rec[i // 3 * 3 + j // 3][ele - 1] = True

        return True