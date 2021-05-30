import collections


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here
        if not start or not end:
            return []

        distance = {}
        dict.add(end)
        dict.add(start)
        self.bfs(end, distance, dict)

        results = []
        self.dfs(start, end, distance, dict, [start], results)
        return results

    def dfs(self, cur, target, distance, dict, path, results):
        if cur == target:
            results.append(path[:])
            return

        for word in self.get_next_word(cur, dict):
            if distance[word] != distance[cur] -1:
                continue
            path.append(word)
            self.dfs(word, target, distance, dict, path, results)
            path.pop()

    def bfs(self, start, distance, dict):
        distance[start] = 0
        queue = collections.deque([start])
        while queue:
            word = queue.popleft()
            for next in self.get_next_word(word, dict):
                if next in distance:
                    continue
                distance[next] = distance[word] +1
                queue.append(next)

    def get_next_word(self, word, dict):
        words = []
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + char + word[i+1:]
                if new_word != word and new_word in dict:
                    words.append(new_word)
        return words