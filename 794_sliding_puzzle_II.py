from collections import deque
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """
    def minMoveStep(self, init_state, final_state):
        # # write your code here
        if not init_state or not final_state:
            return -1

        init_string = self.matrix_to_string(init_state)
        final_string = self.matrix_to_string(final_state)
        queue = deque([init_string])
        distance = {init_string: 0}

        while queue:
            cur = queue.popleft()
            if cur == final_string:
                return distance[final_string]

            for next_state in self.get_next_states(cur):
                if next_state in distance:
                    continue
                queue.append(next_state)
                distance[next_state] = distance[cur] + 1

        return -1
    def get_next_states(self, cur_state):

        zero_index = cur_state.find('0')
        x, y = zero_index//3, zero_index%3
        next_states = []
        for dx, dy in DIRECTIONS:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                next_state = list(cur_state)
                #print(x, y, nx, ny)
                next_state[x*3 + y] = next_state[nx*3 + ny]
                next_state[nx * 3 + ny] = '0'
                next_states.append(''.join(next_state))

        return next_states


    def matrix_to_string(self, mat):
        string = ''
        for row in mat:
            r_str = ''.join([str(x) for x in row])
            string += r_str
        return string

if __name__ == '__main__':
    s = Solution()
    init_state = [
 [2,8,3],
 [1,0,4],
 [7,6,5]
]
    final_state = [
 [1,2,3],
 [8,0,4],
 [7,6,5]
]
    print(s.minMoveStep(init_state, final_state))