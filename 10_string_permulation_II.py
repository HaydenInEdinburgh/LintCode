class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        # write your code here
        if not str:
            return [""]

        chars = sorted(list(str))
        res = []
        visited = [False] * len(str)
        self.dfs(chars, [], visited, res)
        return res

    def dfs(self, chars, path, visited, res):
        if len(path) == len(chars):
            res.append(''.join(path))
            return

        for i in range(len(chars)):
            if visited[i]:
                continue
            if i !=0 and chars[i] == chars[i-1] and not visited[i-1]:
                continue
            visited[i] = True
            path.append(chars[i])
            self.dfs(chars, path, visited, res)
            path.pop()
            visited[i] = False