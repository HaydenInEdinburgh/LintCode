DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # write your code here
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] != word[0]:
                    continue
                visited = {(i, j)}
                #print('start', i, j)
                if self.dfs(word, board, (i, j), 1, visited):
                    return True
        return False

    def dfs(self, word, board, point, index, visited):
        if index >= len(word):
            return True
        x, y = point
        for dx, dy in DIRECTIONS:
            nx, ny = x+dx, y+dy
            if not self.valid(board, nx, ny) or (nx, ny) in visited:
                continue
            #print(board[nx][ny], word[:index+1])
            if board[nx][ny] == word[index]:
                visited.add((nx, ny))
                res = self.dfs(word, board, (nx, ny), index+1, visited)
                visited.remove((nx, ny))
                if res:
                    return True

        return False

    def valid(self, board, x, y):
        return 0<= x<len(board) and 0<= y<len(board[0])

if __name__ == '__main__':
    s = Solution()
    board = ["ABCE","SFCS","ADEE"]
    word = "ABCCED"
    print(s.exist(board, word))