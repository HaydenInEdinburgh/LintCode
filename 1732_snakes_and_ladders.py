from collections import deque
class Solution:
    """
    @param board: board
    @return: snakesAndLadders
    """

    def snakesAndLadders(self, board):
        #
        if not board or not board[0]:
            return -1
        n = len(board)
        total = n*n
        flatten_board = self.flatten(board)
        visited = {1: 0}

        queue = deque([1])
        while queue:
            s = queue.popleft()
            if s == total:
                return visited[s]
            for s2 in range(s+1, min(s+6, total)+1):
                if flatten_board[s2-1] != -1:
                    s2 = flatten_board[s2-1]
                if s2 not in visited:
                    visited[s2] = visited[s] + 1
                    queue.append(s2)

        return -1

    def flatten(self, board):
        flatten_board = []
        for i in range(len(board)-1, -1, -1):
            row = board[i]
            if (i - len(board)) % 2 == 0:
                row = row[::-1]
            flatten_board.extend(row)
        # print(flatten_board)
        return flatten_board

if __name__ == '__main__':
    s = Solution()
    input = [[-1,2,-1],[5,2,2],[-1,-1,-1]]
    print(s.snakesAndLadders(input))