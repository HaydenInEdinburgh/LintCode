from itertools import permutations
class Solution:
    """
    @param num: a array
    @param target: a num
    @return: return all combinations
    """
    def combinationSet(self, num, target):
        # write your code here
        if not num:
            return []

        res = []
        self.dfs(num, target, [], res)
        return res

    def dfs(self, nums, target, path, res):
        if path:
            ans = int(''.join(path))
            if ans >= target:
                return
            else:
                res.append(ans)
        for n in nums:
            if path and path[0] == '0':
                continue
            path.append(str(n))
            self.dfs(nums, target, path, res)
            path.pop()

if __name__ == '__main__':
    s = Solution()
    num = [0,1,2,4]
    target = 30
    print(s.combinationSet(num, target))