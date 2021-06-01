class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        if not n:
            return []

        boards = []
        visited = {
            'col': set(),
            'sum': set(),
            'diff': set(),
        }
        self.dfs(n, boards, visited, [])

        return boards

    def dfs(self, n, boards, visited, path):
        if n == len(path):
            boards.append(self.draw(path[:]))
            return

        row = len(path)
        for col in range(n):
            if not self.is_valid(path, visited, col):
                continue
            path.append(col)
            visited['col'].add(col)
            visited['sum'].add(col+row)
            visited['diff'].add(col-row)
            self.dfs(n, boards, visited, path)
            path.pop()
            visited['col'].remove(col)
            visited['sum'].remove(col+row)
            visited['diff'].remove(col-row)

    def is_valid(self, path, visited, col):
        row = len(path)
        if col in visited['col']:
            return False
        if col + row in visited['sum']:
            return False
        if col - row in visited['diff']:
            return False
        return True

    def draw(self, path):
        # path is like [0, 1, 2, 3] => ['Q...', '.Q..', ...]
        board = []
        n = len(path)
        for col in path:
            row_string = ''.join(['Q' if c == col else '.' for c in range(n)])
            board.append(row_string)

        return board

if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))