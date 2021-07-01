DIRECTIONS = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
from collections import deque
class Solution:
    """
    @param board: a board
    @param click: the position
    @return: the new board
    """
    def updateBoard(self, board, click):
        # Write your code here
        m, n = len(board), len(board[0])
        if not m or not n:
            return []

        for i in range(m):
            board[i] = list(board[i])
        print('1')
        x, y = click[0], click[1]
        if board[x][y] == 'M':
            board[x][y] = 'X'
            self.toString(board)
            return board
        print('2')
        mines = self.get_mines(x, y, board)
        if mines:
            board[x][y] = str(mines)
            self.toString(board)
            return board
        print('3')
        queue = deque([(x, y)])
        board[x][y] = 'B'
        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                nx, ny = x+dx, y+dy
                if not 0 <= nx < len(board) or not 0 <= ny < len(board[0]) or board[nx][ny] != 'E':
                    continue
                cur_mines = self.get_mines(nx, ny, board)
                if cur_mines:
                    board[nx][ny] = str(cur_mines)
                    continue
                queue.append((nx, ny))
                board[nx][ny] = 'B'

        self.toString(board)
        return board


    def get_mines(self, x, y, board):
        mines = 0
        for dx, dy in DIRECTIONS:
            nx, ny = x+dx, y+dy
            if not 0<= nx< len(board) or not 0<= ny< len(board[0]):
                continue
            if board[nx][ny] == 'M':
                mines += 1

        return mines


    def toString(self, board):
        for i in range(len(board)):
            board[i] = ''.join(board[i])

if __name__ == '__main__':
    board = ["EEEEE","EEMEE","EEEEE","EEEEE"]
    click = [3,0]
    s = Solution()
    print(s.updateBoard(board, click))