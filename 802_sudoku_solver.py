class Solution:
    """
    @param board: the sudoku puzzle
    @return: nothing
    """
    def solveSudoku(self, board):
        # write your code here
        used = self.get_initial_used(board)
        self.dfs(board, 0, used)

    def get_initial_used(self, board):
        used = {
            'row': [set() for _ in range(9)],
            'col': [set() for _ in range(9)],
            'box': [set() for _ in range(9)]
        }
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    continue
                used['row'][i].add(board[i][j])
                used['col'][j].add(board[i][j])
                used['box'][i // 3 * 3 + j // 3].add(board[i][j])

        return used

    def dfs(self, board, index, used):
        if index == 81:
            return True
        x, y = index // 9, index % 9
        if board[x][y] != 0:# has filled
            return self.dfs(board, index+1, used)

        for n in range(1, 10):
            if not self.isValid(x, y, used, n):
                continue

            board[x][y] = n
            used['row'][x].add(n)
            used['col'][y].add(n)
            used['box'][x // 3 * 3 + y//3].add(n)
            if self.dfs(board, index+1, used):
                return True
            board[x][y] = 0
            used['row'][x].remove(n)
            used['col'][y].remove(n)
            used['box'][x // 3 * 3 + y//3].remove(n)

        return False

    def isValid(self, x, y, used, n):
        if n in used['row'][x]:
            return False
        if n in used['col'][y]:
            return False
        if n in used['box'][x // 3 * 3 + y//3]:
            return False
        return True

if __name__ == '__main__':
    s = Solution()
    input = [
                [0,0,9,7,4,8,0,0,0],
                [7,0,0,0,0,0,0,0,0],
                [0,2,0,1,0,9,0,0,0],
                [0,0,7,0,0,0,2,4,0],
                [0,6,4,0,1,0,5,9,0],
                [0,9,8,0,0,0,3,0,0],
                [0,0,0,8,0,3,0,2,0],
                [0,0,0,0,0,0,0,0,6],
                [0,0,0,2,7,5,9,0,0]
            ]
    s.solveSudoku(input)
    print(input)