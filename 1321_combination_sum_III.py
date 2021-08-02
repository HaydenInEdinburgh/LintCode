class Solution:
    """
    @param k: an integer
    @param n: an integer
    @return: return a List[List[int]]
    """
    def combinationSum3(self, k, n):
        # write your code here
        if not k or not n:
            return []

        res = []
        self.dfs(1, k, n, [], res,)

        return res

    def dfs(self, start, k, n, path, res):
        if n < 0 or start > 10:
            return

        if len(path) == k and n == 0:
            res.append(path[:])
            return

        for i in range(start, 10):
            path.append(i)
            # print(path)
            self.dfs(i+1, k, n-i, path, res)
            path.pop()

if __name__ == '__main__':
    s = Solution()
    k = 3
    n = 15
    print(s.combinationSum3(k, n))