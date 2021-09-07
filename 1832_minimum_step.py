from collections import deque
class Solution:
    """
    @param colors: the colors of grids
    @return: return the minimum step from position 0 to position n - 1
    """
    def minimumStep(self, colors):
        # write your code here
        if not colors:
            return 0

        start = 0
        visited = {0}
        mapping = self.get_mapping(colors)
        queue = deque([start])
        step = 0

        while queue:
            for _ in range(len(queue)):
                cur_index = queue.popleft()
                cur_color = colors[cur_index]
                if cur_index == len(colors)-1:
                    return step

                for same_color_index in mapping[cur_color]:
                    if same_color_index == cur_index or same_color_index in visited:
                        continue
                    queue.append(same_color_index)
                    visited.add(same_color_index)

                mapping[cur_color] = []
                #dir
                for dx in [1, -1]:
                    new_index = dx + cur_index
                    if new_index < 0 or new_index >= len(colors) or new_index in visited:
                        continue
                    queue.append(new_index)
                    visited.add(new_index)

                #jump
            step += 1

        return -1




    def get_mapping(self, colors):
        mapping = {}
        for i, color in enumerate(colors):
            if color not in mapping:
                mapping[color] = []
            mapping[color].append(i)

        return mapping


if __name__ == '__main__':
    s = Solution()
    grid = [1, 2, 3, 3, 2, 5, 3]
    print(s.minimumStep(grid))