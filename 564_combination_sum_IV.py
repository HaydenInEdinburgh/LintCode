class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackVI(self, nums, target):
        # write your code here
        if not nums:
            return 0

        n = len(nums)
        dp = [0]* (1 + target)
        dp[0] = 1

        for i in range(1, target+1):
            for n in nums:
                if n > i:
                    continue
                dp[i] += dp[i- n]

        return dp[target]

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 4]
    target = 4
    print(s.backPackVI(nums, target))