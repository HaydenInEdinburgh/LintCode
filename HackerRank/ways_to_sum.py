class Solution:
    def ways(self, total, k):
        # Write your code here
        if not k or not total:
            return 0

        dp = [0] * (1 + total)
        dp[0] = 1

        for i in range(1, total + 1):
            for n in range(1, k):
                if n > i:
                    continue
                dp[i] += dp[i - n]

        return dp[total]

    def combinationSum(self, k, total):
        # write your code here
        if not total or not k:
            return []

        res = 0
        self.dfs(k, total, res, 1, [])

        return res % (10**9 + 7)

    def dfs(self, k, target, res, startIndex, path):
        if target < 0:
            return
        if target == 0:
            res += 1
            return

        for i in range(startIndex, k+1):
            path.append(i)
            # print(path)
            self.dfs(k, target - i, res, i, path)
            path.pop()

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum(842, 91))