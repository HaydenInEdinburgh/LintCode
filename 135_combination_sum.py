class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        if not target or not candidates:
            return []

        res = []
        nums = sorted(candidates)
        self.dfs(nums, target, res, 0, [])
        return res

    def dfs(self, candidates, target, res, startIndex, path):
        if target < 0:
            return
        if target == 0:
            res.append(path[:])
            return

        for i in range(startIndex, len(candidates)):
            if i != 0 and candidates[i] == candidates[i-1]:
                continue
            path.append(candidates[i])
            # print(path)
            self.dfs(candidates, target -candidates[i], res, i, path)
            path.pop()


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    expected = [[7], [2, 2, 3]]
    s = Solution()
    output = s.combinationSum(candidates, target)
    print(output)