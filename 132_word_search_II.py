DIRECTION = [(1, 0), (-1, 0), (0, -1), (0, 1)]
class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        if not board or not words:
            return []

        prefix_set = self.get_prefix_set(words)
        word_set = set(words)

        res = set()
        for x in range(len(board)):
            for y in range(len(board[0])):
                visited = {(x, y)}
                self.search(board, x, y, board[x][y], visited, prefix_set, word_set, res)
        return list(res)

    def search(self, board, x, y, word, visited, prefix_set, word_set, res):
        if word not in prefix_set:
            return
        if word in word_set:
            res.add(word)

        for dx, dy in DIRECTION:
            nx, ny = x+dx, y+dy
            if not self.isValid(board, nx, ny):
                continue
            if (nx, ny) in visited:
                continue
            visited.add((nx, ny))
            self.search(board, nx, ny, word + board[nx][ny], visited, prefix_set, word_set, res)
            visited.remove((nx, ny))


    def get_prefix_set(self, words):
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
                if word[:i+1] not in prefix_set:
                    prefix_set.add(word[:i+1])
        return prefix_set

    def isValid(self, board, x, y):
        return 0<= x< len(board) and 0<= y< len(board[0])

if __name__ == '__main__':
    board = ["b","a","b","b","a"]
    words = ["babbab","b","a","ba"]
    expected = ["a","b","ba"]
    print(Solution().wordSearchII(board, words))