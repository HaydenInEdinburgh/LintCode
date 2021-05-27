import collections

# BFS (Similar to Number of Islands)
class Solution:
    """
    @param image: a 2-D array
    @param sr: an integer
    @param sc: an integer
    @param newColor: an integer
    @return: the modified image
    """

    def floodFill(self, image, sr, sc, newColor):
        # Write your code here
        if not image or not image[0]:
            return
        startColor = image[sr][sc]
        queue = collections.deque([(sr, sc)])
        visited = {(sr, sc)}
        image[sr][sc] = newColor
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) in visited:
                    continue
                if not self.ifValid(image, nx, ny, startColor):
                    continue
                image[nx][ny] = newColor
                queue.append((nx, ny))
                visited.add((nx, ny))

        return image

    def ifValid(self, image, x, y, startColor):
        m, n = len(image), len(image[0])
        if not (0 <= x < m and 0 <= y < n):
            return False
        return image[x][y] == startColor
