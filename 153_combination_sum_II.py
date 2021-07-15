class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here
        if not num:
            return []
        num.sort()
        res, used = [], [0] * len(num)
        self.dfs(num, target, 0, 0, [], res, used)
        return list(res)

    def dfs(self, num, target, cur, start, path, res, used):
        #print(cur, path)
        if cur == target:
            res.append(path[:])
            return
        for i_next in range(start, len(num)):
            if num[i_next]+ cur <= target and (i_next ==0 or num[i_next] != num[i_next-1] or used[i_next-1]):
                path.append(num[i_next])
                used[i_next] = 1
                self.dfs(num, target, cur + num[i_next], i_next+1, path, res, used)
                path.pop()
                used[i_next] = 0



if __name__ == '__main__':
    s = Solution()
    target = 7
    nums = [2,3,6,7]
    print(s.combinationSum2(nums, target))