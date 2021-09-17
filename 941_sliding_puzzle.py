from collections import deque

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Solution:
    """
    @param board: the given board
    @return:  the least number of moves required so that the state of the board is solved
    """

    def slidingPuzzle(self, board):
        # write your code here
        if not board:
            return 0

        target = '123450'
        source = self.mat_to_str(board)
        queue = deque([source])
        step = 0
        visited = {source}
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == target:
                    return step

                for next_state in self.get_next_states(cur):
                    if next_state in visited:
                        continue
                    queue.append(next_state)
                    visited.add(next_state)
            step += 1
        return -1


    def mat_to_str(self, board):
        string = ''
        m = len(board)
        for i in range(m):
            string += ''.join([str(x) for x in board[i]])
        return string

    def get_next_states(self, cur_state):

        zero_index = cur_state.find('0')
        x, y = zero_index//3, zero_index % 3
        next_states = []
        for dx, dy in DIRECTIONS:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 2 and 0 <= ny < 3:
                next_state = list(cur_state)
                # print(next_state)
                # print(x, y, nx, ny)
                next_state[x*3 + y] = next_state[nx*3 + ny]
                next_state[nx * 3 + ny] = '0'
                next_states.append(''.join(next_state))

        return next_states
if __name__ == '__main__':
    s = Solution()
    board = [[1, 2, 3], [4, 0, 5]]
    print(s.slidingPuzzle(board))
